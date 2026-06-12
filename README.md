# Internship Task 1 - Nested JSON Data Extraction and Relationship Analysis

## Objective

The objective of this task is to read a nested JSON file, transform the hierarchical data into a relational structure, and establish relationships between parent and child entities.

The implementation performs the following:

* Reads the nested JSON file.
* Stores the root-level entity as a parent table.
* Extracts nested child entities into separate views.
* Maintains relationships using the parent key (`eventId`).
* Analyzes and documents entity relationships.

---

## Technology Stack

* Python 3
* Pandas
* JSON
* CSV

---

## Project Structure

```text
Internship_Task_1/
│
├── input/
│   └── matrixx_purchasemm_event.json
│
├── output/
│   ├── purchase_event.csv
│   ├── api_event_data_view.csv
│   ├── api_event_security_info_view.csv
│   ├── primary_event_attr_view.csv
│   ├── applied_catalog_item_view.csv
│   ├── catalog_item_parameter_view.csv
│   ├── applied_offer_view.csv
│   ├── balance_update_view.csv
│   ├── charge_view.csv
│   └── offer_info_view.csv
│
├── README.md
└── main.py
```

---

## Parent Table

The root JSON object (`MtxPurchaseEvent`) was modeled as the parent entity.

### Table: `purchase_event`

Primary Key:

```text
eventId
```

The table contains all scalar (non-object and non-array) attributes from the root JSON.

Example fields:

* eventId
* eventTime
* tenantId
* walletId
* initiatorId
* initiatorType
* taxLocation
* taxStatus
* walletOwnerId
* walletOwnerType

---

## Child Views

Nested objects and arrays were extracted into separate views.

Each child view contains the parent identifier (`eventId`) to preserve the relationship with the parent table.

| View Name                    | Source JSON Element       |
| ---------------------------- | ------------------------- |
| api_event_data_view          | apiEventData              |
| api_event_security_info_view | apiEventSecurityInfo      |
| primary_event_attr_view      | primaryEventAttr          |
| applied_catalog_item_view    | appliedCatalogItemArray   |
| catalog_item_parameter_view  | catalogItemParameterArray |
| applied_offer_view           | appliedOfferArray         |
| balance_update_view          | balanceUpdateArray        |
| charge_view                  | chargeList                |
| offer_info_view              | offerInfoArray            |

---

## Relationship Analysis

### Cardinality Determination
Relationship cardinality was determined based on the JSON structure:

* A nested JSON object (`{}`) represents a single child entity and was modeled as a **1:1 relationship**.
* A nested JSON array (`[]`) represents a collection of child entities and was modeled as a **1:N relationship**.

### Relationship Matrix

| Parent Entity      | Child Entity         | Cardinality |
| ------------------ | -------------------- | ----------- |
| PurchaseEvent      | ApiEventData         | 1:1         |
| PurchaseEvent      | ApiEventSecurityInfo | 1:1         |
| PurchaseEvent      | PrimaryEventAttr     | 1:1         |
| PurchaseEvent      | AppliedCatalogItem   | 1:N         |
| AppliedCatalogItem | CatalogItemParameter | 1:N         |
| PurchaseEvent      | AppliedOffer         | 1:N         |
| PurchaseEvent      | BalanceUpdate        | 1:N         |
| PurchaseEvent      | Charge               | 1:N         |
| PurchaseEvent      | OfferInfo            | 1:N         |

---

## Entity Hierarchy

```text
PurchaseEvent (eventId)
│
├── ApiEventData (1:1)
├── ApiEventSecurityInfo (1:1)
├── PrimaryEventAttr (1:1)
│
├── AppliedCatalogItem (1:N)
│     └── CatalogItemParameter (1:N)
│
├── AppliedOffer (1:N)
├── BalanceUpdate (1:N)
├── Charge (1:N)
└── OfferInfo (1:N)
```

---

## Additional Cross-Entity References

Apart from the parent-child hierarchy, the JSON contains index-based references that establish relationships between child entities.

### AppliedOffer → AppliedCatalogItem

Field:

```json
"appliedCatalogItemIndex": 0
```

This field links an applied offer to a corresponding catalog item.

---

### Charge → AppliedOffer

Field:

```json
"appliedOfferIndex": 0
```

This field links a charge record to the applied offer that generated the charge.

---

### Charge → BalanceUpdate

Field:

```json
"balanceUpdateIndex": 0
```

This field links a charge record to the corresponding balance update.

These references provide additional business-level relationships beyond the primary parent-child hierarchy.

---

## Output

The solution generates the following output files:

```text
purchase_event.csv

api_event_data_view.csv
api_event_security_info_view.csv
primary_event_attr_view.csv

applied_catalog_item_view.csv
catalog_item_parameter_view.csv

applied_offer_view.csv
balance_update_view.csv
charge_view.csv
offer_info_view.csv
```

All child views include the parent identifier (`eventId`) to ensure records remain accessible through the parent entity.

---

## Conclusion

The nested purchase event JSON was successfully transformed into a relational structure consisting of one parent table and multiple child views. Parent-child relationships, nested relationships, and cross-entity references were identified and preserved, enabling efficient querying, reporting, and further analytical processing of the data.
