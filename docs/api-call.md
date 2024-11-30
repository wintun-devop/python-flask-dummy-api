## API Call using javascript fetch
### login api
```
 const resp = await fetch(urlImportFromENV, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        "user_name":"wintun.edu@gmail.com",
        "user_password":"abc123!@#"
      }),
      cache: "no-store",
});
```
### register api
```
 const resp = await fetch(urlImportFromENV, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        "user_name":"wintun.edu@gmail.com",
        "user_password":"abc123!@#",
        "user_custom_id":"ufakfaf",
        "user_name":"ufkfaf"
      }),
      cache: "no-store",
});
```
### get all
```
const resp = await fetch(urlImportFromENV, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",  
      },
      cache: "no-store",
});
```