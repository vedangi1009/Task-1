import json
import pandas as pd

with open("matrixx_purchasemm_event.json", "r") as f:
    data = json.load(f)

parent = {}

for key, value in data.items():
    if not isinstance(value, (dict, list)):
        parent[key] = value

purchase_event_df = pd.DataFrame([parent])

print(purchase_event_df)

purchase_event_df.to_csv("purchase_event.csv", index=False)

security_df = pd.DataFrame([{
    "eventId": data["eventId"],
    **data["apiEventSecurityInfo"]
}])

print("\nSecurity View:")
print(security_df)

security_df.to_csv(
    "api_event_security_info_view.csv",
    index=False
)

api_event_data_df = pd.DataFrame([{
    "eventId": data["eventId"],
    **data["apiEventData"]
}])

api_event_data_df.to_csv(
    "api_event_data_view.csv",
    index=False
)

print("\nAPI Event Data View:")
print(api_event_data_df)

primary_event_attr_df = pd.DataFrame([{
    "eventId": data["eventId"],
    **data["primaryEventAttr"]
}])

primary_event_attr_df.to_csv(
    "primary_event_attr_view.csv",
    index=False
)

print("\nPrimary Event Attr View:")
print(primary_event_attr_df)

offer_records = []

for offer in data["appliedOfferArray"]:

    offer_records.append({
        "eventId": data["eventId"],
        **offer
    })

offer_df = pd.DataFrame(offer_records)

print("\nApplied Offer View:")
print(offer_df)

offer_df.to_csv(
    "applied_offer_view.csv",
    index=False
)

balance_records = []

for balance in data["balanceUpdateArray"]:

    balance_records.append({
        "eventId": data["eventId"],
        **balance
    })

balance_df = pd.DataFrame(balance_records)

balance_df.to_csv(
    "balance_update_view.csv",
    index=False
)

print(balance_df)

offer_info_records = []

for offer_info in data["offerInfoArray"]:

    offer_info_records.append({
        "eventId": data["eventId"],
        **offer_info
    })

offer_info_df = pd.DataFrame(offer_info_records)

offer_info_df.to_csv(
    "offer_info_view.csv",
    index=False
)

print(offer_info_df)

catalog_item_records = []

for item in data["appliedCatalogItemArray"]:

    catalog_item_records.append({
        "eventId": data["eventId"],
        "catalogItemId": item["catalogItemId"],
        "catalogItemExternalId": item["catalogItemExternalId"]
    })

catalog_item_df = pd.DataFrame(catalog_item_records)

catalog_item_df.to_csv(
    "applied_catalog_item_view.csv",
    index=False
)

print(catalog_item_df)

parameter_records = []

for item in data["appliedCatalogItemArray"]:

    catalog_item_id = item["catalogItemId"]

    for parameter in item["catalogItemParameterArray"]:

        parameter_records.append({
            "eventId": data["eventId"],
            "catalogItemId": catalog_item_id,
            "parameterDefnId": parameter["parameterDefnId"],
            "parameterName": parameter["parameterName"],
            "valueType": parameter["valueType"],
            "value": parameter["value"]["value"]
        })

parameter_df = pd.DataFrame(parameter_records)

parameter_df.to_csv(
    "catalog_item_parameter_view.csv",
    index=False
)

print(parameter_df)