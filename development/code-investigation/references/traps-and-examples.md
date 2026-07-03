# Common Traps & Examples

Reference material for the code-investigation skill. Read this when you need detailed guidance on avoiding mistakes or want to see a worked example.

---

## Common Traps

| # | Trap | Signal | Correction |
|---|------|--------|-----------|
| 1 | **Shallow exploration** | Conclusions drawn from wrapper classes or entry points without tracing to actual data definitions | Chase every dynamic/generic field to its producer. If you don't know the runtime type, you can't claim you do. |
| 2 | **Doc-driven conclusions** | Claims sourced from README/Wiki/design docs without code verification | Treat all docs as hypotheses. Use code to confirm or refute. |
| 3 | **Single-module tunnel vision** | Multi-module system analyzed by reading only one module | Map the full data flow across all participating modules, especially serialization boundaries. |
| 4 | **Ignoring schema evolution** | Early schema scripts treated as current state | Always look at the final state (runtime type definitions), not just creation scripts. |
| 5 | **Single-perspective blind spot** | Pure engineer viewpoint — missing ops feasibility, security, business continuity | After technical work, review from 2-3 additional role perspectives. |
| 6 | **Unvalidated proposals** | Plans that sound reasonable but have unverified preconditions (e.g., "reverse sync" without checking schema compatibility) | For every proposal, ask: "what are the exact steps if we execute today? Are all preconditions met?" |
| 7 | **Cross-document inconsistency** | One doc updated, others still show old info; pseudocode names differ from actual code | After any revision, sweep all docs that reference the changed information. |
| 8 | **Optimism bias** | Time estimates only account for happy path | Add 30-50% buffer. Identify external dependencies as independent risk items. Distinguish "dev done" from "delivery ready." |
| 9 | **Missing edge data** | Only main-flow data analyzed; caches, config, permissions, extensions overlooked | After main analysis, explicitly ask: "what other data participates in this system's operation?" Inventory all storage mediums. |

---

## Example: Tracing an Untyped Field

Scenario: You encounter a field declared as a generic/untyped container (e.g., `payload: Object`).

**Wrong approach:**
> "The `payload` field stores order details as a JSON object with fields like orderId, lineItems, etc."
> *(Based on: reading an internal wiki page that describes the expected format)*

**Correct approach:**

1. Find who writes to this field:
   ```
   → OrderEventPublisher.publish() sets payload = serialize(enrichedOrder)
   ```
2. Check what `enrichedOrder` actually is:
   ```
   → enrichedOrder is of type SalesOrderDetail, defined in sales-module/src/.../SalesOrderDetail
   ```
3. Read SalesOrderDetail's actual fields:
   ```
   → header: OrderHeader (orderId, orderDate, customerId, status, ...)
   → lineItems: List<LineItem> (productId, quantity, unitPrice, discount, ...)
   → shipment: ShipmentInfo (shipMethod, trackingNumber, carrier)
   ```
4. Check how it's serialized:
   ```
   → Framework uses camelCase field naming by default
   → Enums serialize as string names (e.g., "SHIPPED"), not ordinals
   → Dates serialize as ISO-8601 strings
   ```
5. Document with confidence level:
   > **Confirmed** (source: `sales-module/.../SalesOrderDetail`, `event-service/.../OrderEventPublisher.publish()`):
   > The `payload` field contains a serialized `SalesOrderDetail` with nested `header`, `lineItems[]`, and `shipment` structures.

This approach takes 5 minutes longer but prevents the kind of error where you document field names that don't actually exist in the stored data.

---

## Example: Detecting Schema Evolution

Scenario: You see a database migration `V002__create_product.sql` that creates the `Product` table with 5 columns.

**Wrong approach:**
> "The Product table has 5 columns: ProductID, Name, ProductNumber, ListPrice, ModifiedDate."

**Correct approach:**

1. Check for later migrations:
   ```
   V002__create_product.sql           ← initial creation
   V014__add_product_category.sql     ← adds CategoryID column + FK
   V027__add_product_inventory.sql    ← adds SafetyStockLevel, ReorderPoint
   V031__rename_to_product_catalog.sql ← renames table
   ```
2. Look at the runtime type definition (the entity/model class) to see the CURRENT state
3. Document:
   > **Confirmed** (source: `ProductCatalog` entity class, migrations `V002` + `V014` + `V027` + `V031`):
   > The table is now `product_catalog` with 8 columns including `category_id`, `safety_stock_level`, and `reorder_point`.

---

## Quick-Reference: Confidence Labels

Use these when documenting findings:

| Label | Meaning | When to use |
|-------|---------|-------------|
| **Confirmed** | Verified by reading source code at both producer and consumer | Default for most findings |
| **Inferred** | Deduced from partial evidence (e.g., only saw consumer, not producer) | When you can't access both ends |
| **Assumed** | Based on convention or documentation, not verified in code | When code is unavailable (binary deps, external services) |
| **Unknown** | Could not determine | Be honest about gaps |
