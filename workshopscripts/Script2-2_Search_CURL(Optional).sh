curl -X POST "https://support-lab-be.glean.com/rest/api/v1/search" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <SEARCH_API_TOKEN>" \
  -d '{
    "query": "GleanPartnerWorkshop_Example_Document",
    "limit": 10,
    "datasource": "gleanpartnerworkshop"
}'