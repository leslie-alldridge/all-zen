# all-zen

zendesk

1. virtualenv env
2. .\env\scripts\activate

## comment on a ticket

https://github.com/facetoe/zenpy#commenting-on-a-ticket

## wrapper possibility

https://github.com/facetoe/zenpy

## to close the ticket

```
curl https://{subdomain}.zendesk.com/api/v2/tickets/{id}.json \
  -H "Content-Type: application/json" \
  -d '{"ticket": {"status": "open", "comment": { "body": "The smoke is very colorful.", "author_id": 494820284 }}}' \
  -v -u {email_address}:{password} -X PUT
```

Need to receive ticket and edit status to solved / closed then post it back as a PUT request
