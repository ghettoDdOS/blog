---
title: Blog API v1.0.0
language_tabs:
  - shell: Shell
toc_footers: []
includes: []
search: true
highlight_theme: darkula
headingLevel: 2

---

<!-- Generator: Widdershins v4.0.1 -->

<h1 id="blog-api">Blog API v1.0.0</h1>

> Scroll down for code samples, example requests and responses. Select a language for code samples from the tabs above or the mobile navigation menu.

Blog

# Authentication

- HTTP Authentication, scheme: bearer 

<h1 id="blog-api-authors">authors</h1>

## authors_list

<a id="opIdauthors_list"></a>

> Code samples

```shell
curl --request GET \
  --url https://example.com/api/authors/ \
  --header 'Accept: application/json' \
  --header 'Authorization: Bearer {access-token}'
```

`GET /api/authors/`

<h3 id="authors_list-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|page|query|integer|false|A page number within the paginated result set.|

> Example responses

> 200 Response

```json
{
  "count": 123,
  "next": "http://api.example.org/accounts/?page=4",
  "previous": "http://api.example.org/accounts/?page=2",
  "results": [
    {
      "id": 0,
      "first_name": "string",
      "last_name": "string",
      "email": "user@example.com",
      "phone": "string",
      "registration_date": "string"
    }
  ]
}
```

<h3 id="authors_list-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|[PaginatedAuthorList](#schemapaginatedauthorlist)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
jwtAuth
</aside>

## authors_profile_retrieve

<a id="opIdauthors_profile_retrieve"></a>

> Code samples

```shell
curl --request GET \
  --url https://example.com/api/authors/profile/ \
  --header 'Accept: application/json' \
  --header 'Authorization: Bearer {access-token}'
```

`GET /api/authors/profile/`

> Example responses

> 200 Response

```json
{
  "id": 0,
  "first_name": "string",
  "last_name": "string",
  "email": "user@example.com",
  "phone": "string",
  "registration_date": "string"
}
```

<h3 id="authors_profile_retrieve-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|[Author](#schemaauthor)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
jwtAuth
</aside>

## authors_profile_update

<a id="opIdauthors_profile_update"></a>

> Code samples

```shell
curl --request PUT \
  --url https://example.com/api/authors/profile/ \
  --header 'Accept: application/json' \
  --header 'Authorization: Bearer {access-token}' \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --data ''
```

`PUT /api/authors/profile/`

> Body parameter

```json
{
  "first_name": "string",
  "last_name": "string",
  "email": "user@example.com",
  "password": "string",
  "password_confirmation": "string",
  "phone": "string"
}
```

```yaml
first_name: string
last_name: string
email: user@example.com
password: string
password_confirmation: string
phone: string

```

<h3 id="authors_profile_update-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[Author](#schemaauthor)|true|none|

> Example responses

> 200 Response

```json
{
  "id": 0,
  "first_name": "string",
  "last_name": "string",
  "email": "user@example.com",
  "phone": "string",
  "registration_date": "string"
}
```

<h3 id="authors_profile_update-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|[Author](#schemaauthor)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
jwtAuth
</aside>

## authors_profile_partial_update

<a id="opIdauthors_profile_partial_update"></a>

> Code samples

```shell
curl --request PATCH \
  --url https://example.com/api/authors/profile/ \
  --header 'Accept: application/json' \
  --header 'Authorization: Bearer {access-token}' \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --data ''
```

`PATCH /api/authors/profile/`

> Body parameter

```json
{
  "first_name": "string",
  "last_name": "string",
  "email": "user@example.com",
  "password": "string",
  "password_confirmation": "string",
  "phone": "string"
}
```

```yaml
first_name: string
last_name: string
email: user@example.com
password: string
password_confirmation: string
phone: string

```

<h3 id="authors_profile_partial_update-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[PatchedAuthor](#schemapatchedauthor)|false|none|

> Example responses

> 200 Response

```json
{
  "id": 0,
  "first_name": "string",
  "last_name": "string",
  "email": "user@example.com",
  "phone": "string",
  "registration_date": "string"
}
```

<h3 id="authors_profile_partial_update-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|[Author](#schemaauthor)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
jwtAuth
</aside>

## authors_profile_destroy

<a id="opIdauthors_profile_destroy"></a>

> Code samples

```shell
curl --request DELETE \
  --url https://example.com/api/authors/profile/ \
  --header 'Authorization: Bearer {access-token}'
```

`DELETE /api/authors/profile/`

<h3 id="authors_profile_destroy-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|204|[No Content](https://tools.ietf.org/html/rfc7231#section-6.3.5)|No response body|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
jwtAuth
</aside>

## authors_registration_create

<a id="opIdauthors_registration_create"></a>

> Code samples

```shell
curl --request POST \
  --url https://example.com/api/authors/registration/ \
  --header 'Accept: application/json' \
  --header 'Authorization: Bearer {access-token}' \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --data ''
```

`POST /api/authors/registration/`

> Body parameter

```json
{
  "first_name": "string",
  "last_name": "string",
  "email": "user@example.com",
  "password": "string",
  "password_confirmation": "string",
  "phone": "string"
}
```

```yaml
first_name: string
last_name: string
email: user@example.com
password: string
password_confirmation: string
phone: string

```

<h3 id="authors_registration_create-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[Author](#schemaauthor)|true|none|

> Example responses

> 201 Response

```json
{
  "id": 0,
  "first_name": "string",
  "last_name": "string",
  "email": "user@example.com",
  "phone": "string",
  "registration_date": "string"
}
```

<h3 id="authors_registration_create-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|none|[Author](#schemaauthor)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
jwtAuth, None
</aside>

<h1 id="blog-api-blogs">blogs</h1>

## blogs_list

<a id="opIdblogs_list"></a>

> Code samples

```shell
curl --request GET \
  --url https://example.com/api/blogs/ \
  --header 'Accept: application/json' \
  --header 'Authorization: Bearer {access-token}'
```

`GET /api/blogs/`

<h3 id="blogs_list-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|page|query|integer|false|A page number within the paginated result set.|

> Example responses

> 200 Response

```json
{
  "count": 123,
  "next": "http://api.example.org/accounts/?page=4",
  "previous": "http://api.example.org/accounts/?page=2",
  "results": [
    {
      "author": {
        "id": 0,
        "first_name": "string",
        "last_name": "string",
        "email": "user@example.com",
        "phone": "string",
        "registration_date": "string"
      },
      "title": "string",
      "content": "string",
      "created_at": "2019-08-24T14:15:22Z"
    }
  ]
}
```

<h3 id="blogs_list-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|[PaginatedBlogList](#schemapaginatedbloglist)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
jwtAuth
</aside>

## blogs_create

<a id="opIdblogs_create"></a>

> Code samples

```shell
curl --request POST \
  --url https://example.com/api/blogs/ \
  --header 'Accept: application/json' \
  --header 'Authorization: Bearer {access-token}' \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --data ''
```

`POST /api/blogs/`

> Body parameter

```json
{
  "title": "string",
  "content": "string"
}
```

```yaml
title: string
content: string

```

<h3 id="blogs_create-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[Blog](#schemablog)|true|none|

> Example responses

> 201 Response

```json
{
  "author": {
    "id": 0,
    "first_name": "string",
    "last_name": "string",
    "email": "user@example.com",
    "phone": "string",
    "registration_date": "string"
  },
  "title": "string",
  "content": "string",
  "created_at": "2019-08-24T14:15:22Z"
}
```

<h3 id="blogs_create-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|none|[Blog](#schemablog)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
jwtAuth
</aside>

## blogs_retrieve

<a id="opIdblogs_retrieve"></a>

> Code samples

```shell
curl --request GET \
  --url https://example.com/api/blogs/0/ \
  --header 'Accept: application/json' \
  --header 'Authorization: Bearer {access-token}'
```

`GET /api/blogs/{id}/`

<h3 id="blogs_retrieve-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|integer|true|A unique integer value identifying this Блог.|

> Example responses

> 200 Response

```json
{
  "author": {
    "id": 0,
    "first_name": "string",
    "last_name": "string",
    "email": "user@example.com",
    "phone": "string",
    "registration_date": "string"
  },
  "title": "string",
  "content": "string",
  "created_at": "2019-08-24T14:15:22Z"
}
```

<h3 id="blogs_retrieve-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|[Blog](#schemablog)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
jwtAuth
</aside>

## blogs_update

<a id="opIdblogs_update"></a>

> Code samples

```shell
curl --request PUT \
  --url https://example.com/api/blogs/0/ \
  --header 'Accept: application/json' \
  --header 'Authorization: Bearer {access-token}' \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --data ''
```

`PUT /api/blogs/{id}/`

> Body parameter

```json
{
  "title": "string",
  "content": "string"
}
```

```yaml
title: string
content: string

```

<h3 id="blogs_update-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|integer|true|A unique integer value identifying this Блог.|
|body|body|[Blog](#schemablog)|true|none|

> Example responses

> 200 Response

```json
{
  "author": {
    "id": 0,
    "first_name": "string",
    "last_name": "string",
    "email": "user@example.com",
    "phone": "string",
    "registration_date": "string"
  },
  "title": "string",
  "content": "string",
  "created_at": "2019-08-24T14:15:22Z"
}
```

<h3 id="blogs_update-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|[Blog](#schemablog)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
jwtAuth
</aside>

## blogs_partial_update

<a id="opIdblogs_partial_update"></a>

> Code samples

```shell
curl --request PATCH \
  --url https://example.com/api/blogs/0/ \
  --header 'Accept: application/json' \
  --header 'Authorization: Bearer {access-token}' \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --data ''
```

`PATCH /api/blogs/{id}/`

> Body parameter

```json
{
  "title": "string",
  "content": "string"
}
```

```yaml
title: string
content: string

```

<h3 id="blogs_partial_update-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|integer|true|A unique integer value identifying this Блог.|
|body|body|[PatchedBlog](#schemapatchedblog)|false|none|

> Example responses

> 200 Response

```json
{
  "author": {
    "id": 0,
    "first_name": "string",
    "last_name": "string",
    "email": "user@example.com",
    "phone": "string",
    "registration_date": "string"
  },
  "title": "string",
  "content": "string",
  "created_at": "2019-08-24T14:15:22Z"
}
```

<h3 id="blogs_partial_update-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|[Blog](#schemablog)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
jwtAuth
</aside>

## blogs_destroy

<a id="opIdblogs_destroy"></a>

> Code samples

```shell
curl --request DELETE \
  --url https://example.com/api/blogs/0/ \
  --header 'Authorization: Bearer {access-token}'
```

`DELETE /api/blogs/{id}/`

<h3 id="blogs_destroy-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|integer|true|A unique integer value identifying this Блог.|

<h3 id="blogs_destroy-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|204|[No Content](https://tools.ietf.org/html/rfc7231#section-6.3.5)|No response body|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
jwtAuth
</aside>

<h1 id="blog-api-comments">comments</h1>

## comments_list

<a id="opIdcomments_list"></a>

> Code samples

```shell
curl --request GET \
  --url https://example.com/api/comments/ \
  --header 'Accept: application/json' \
  --header 'Authorization: Bearer {access-token}'
```

`GET /api/comments/`

<h3 id="comments_list-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|page|query|integer|false|A page number within the paginated result set.|

> Example responses

> 200 Response

```json
{
  "count": 123,
  "next": "http://api.example.org/accounts/?page=4",
  "previous": "http://api.example.org/accounts/?page=2",
  "results": [
    {
      "author": {
        "id": 0,
        "first_name": "string",
        "last_name": "string",
        "email": "user@example.com",
        "phone": "string",
        "registration_date": "string"
      },
      "blog": 0,
      "content": "string",
      "created_at": "2019-08-24T14:15:22Z"
    }
  ]
}
```

<h3 id="comments_list-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|[PaginatedCommentList](#schemapaginatedcommentlist)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
jwtAuth
</aside>

## comments_create

<a id="opIdcomments_create"></a>

> Code samples

```shell
curl --request POST \
  --url https://example.com/api/comments/ \
  --header 'Accept: application/json' \
  --header 'Authorization: Bearer {access-token}' \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --data ''
```

`POST /api/comments/`

> Body parameter

```json
{
  "blog": 0,
  "content": "string"
}
```

```yaml
blog: 0
content: string

```

<h3 id="comments_create-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[Comment](#schemacomment)|true|none|

> Example responses

> 201 Response

```json
{
  "author": {
    "id": 0,
    "first_name": "string",
    "last_name": "string",
    "email": "user@example.com",
    "phone": "string",
    "registration_date": "string"
  },
  "blog": 0,
  "content": "string",
  "created_at": "2019-08-24T14:15:22Z"
}
```

<h3 id="comments_create-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|none|[Comment](#schemacomment)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
jwtAuth
</aside>

## comments_retrieve

<a id="opIdcomments_retrieve"></a>

> Code samples

```shell
curl --request GET \
  --url https://example.com/api/comments/0/ \
  --header 'Accept: application/json' \
  --header 'Authorization: Bearer {access-token}'
```

`GET /api/comments/{id}/`

<h3 id="comments_retrieve-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|integer|true|A unique integer value identifying this Комментарий.|

> Example responses

> 200 Response

```json
{
  "author": {
    "id": 0,
    "first_name": "string",
    "last_name": "string",
    "email": "user@example.com",
    "phone": "string",
    "registration_date": "string"
  },
  "blog": 0,
  "content": "string",
  "created_at": "2019-08-24T14:15:22Z"
}
```

<h3 id="comments_retrieve-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|[Comment](#schemacomment)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
jwtAuth
</aside>

## comments_update

<a id="opIdcomments_update"></a>

> Code samples

```shell
curl --request PUT \
  --url https://example.com/api/comments/0/ \
  --header 'Accept: application/json' \
  --header 'Authorization: Bearer {access-token}' \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --data ''
```

`PUT /api/comments/{id}/`

> Body parameter

```json
{
  "blog": 0,
  "content": "string"
}
```

```yaml
blog: 0
content: string

```

<h3 id="comments_update-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|integer|true|A unique integer value identifying this Комментарий.|
|body|body|[Comment](#schemacomment)|true|none|

> Example responses

> 200 Response

```json
{
  "author": {
    "id": 0,
    "first_name": "string",
    "last_name": "string",
    "email": "user@example.com",
    "phone": "string",
    "registration_date": "string"
  },
  "blog": 0,
  "content": "string",
  "created_at": "2019-08-24T14:15:22Z"
}
```

<h3 id="comments_update-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|[Comment](#schemacomment)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
jwtAuth
</aside>

## comments_partial_update

<a id="opIdcomments_partial_update"></a>

> Code samples

```shell
curl --request PATCH \
  --url https://example.com/api/comments/0/ \
  --header 'Accept: application/json' \
  --header 'Authorization: Bearer {access-token}' \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --data ''
```

`PATCH /api/comments/{id}/`

> Body parameter

```json
{
  "blog": 0,
  "content": "string"
}
```

```yaml
blog: 0
content: string

```

<h3 id="comments_partial_update-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|integer|true|A unique integer value identifying this Комментарий.|
|body|body|[PatchedComment](#schemapatchedcomment)|false|none|

> Example responses

> 200 Response

```json
{
  "author": {
    "id": 0,
    "first_name": "string",
    "last_name": "string",
    "email": "user@example.com",
    "phone": "string",
    "registration_date": "string"
  },
  "blog": 0,
  "content": "string",
  "created_at": "2019-08-24T14:15:22Z"
}
```

<h3 id="comments_partial_update-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|[Comment](#schemacomment)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
jwtAuth
</aside>

## comments_destroy

<a id="opIdcomments_destroy"></a>

> Code samples

```shell
curl --request DELETE \
  --url https://example.com/api/comments/0/ \
  --header 'Authorization: Bearer {access-token}'
```

`DELETE /api/comments/{id}/`

<h3 id="comments_destroy-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|integer|true|A unique integer value identifying this Комментарий.|

<h3 id="comments_destroy-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|204|[No Content](https://tools.ietf.org/html/rfc7231#section-6.3.5)|No response body|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
jwtAuth
</aside>

<h1 id="blog-api-token">token</h1>

## token_create

<a id="opIdtoken_create"></a>

> Code samples

```shell
curl --request POST \
  --url https://example.com/api/token/ \
  --header 'Accept: application/json' \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --data ''
```

`POST /api/token/`

Takes a set of user credentials and returns an access and refresh JSON web
token pair to prove the authentication of those credentials.

> Body parameter

```json
{
  "email": "string",
  "password": "string"
}
```

```yaml
email: string
password: string

```

<h3 id="token_create-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[TokenObtainPair](#schematokenobtainpair)|true|none|

> Example responses

> 200 Response

```json
{
  "access": "string",
  "refresh": "string"
}
```

<h3 id="token_create-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|[TokenObtainPair](#schematokenobtainpair)|

<aside class="success">
This operation does not require authentication
</aside>

## token_refresh_create

<a id="opIdtoken_refresh_create"></a>

> Code samples

```shell
curl --request POST \
  --url https://example.com/api/token/refresh/ \
  --header 'Accept: application/json' \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --data ''
```

`POST /api/token/refresh/`

Takes a refresh type JSON web token and returns an access type JSON web
token if the refresh token is valid.

> Body parameter

```json
{
  "refresh": "string"
}
```

```yaml
refresh: string

```

<h3 id="token_refresh_create-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[TokenRefresh](#schematokenrefresh)|true|none|

> Example responses

> 200 Response

```json
{
  "access": "string"
}
```

<h3 id="token_refresh_create-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|[TokenRefresh](#schematokenrefresh)|

<aside class="success">
This operation does not require authentication
</aside>

## token_verify_create

<a id="opIdtoken_verify_create"></a>

> Code samples

```shell
curl --request POST \
  --url https://example.com/api/token/verify/ \
  --header 'Accept: application/json' \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --data ''
```

`POST /api/token/verify/`

Takes a token and indicates if it is valid.  This view provides no
information about a token's fitness for a particular use.

> Body parameter

```json
{
  "token": "string"
}
```

```yaml
token: string

```

<h3 id="token_verify_create-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[TokenVerify](#schematokenverify)|true|none|

> Example responses

> 200 Response

```json
{}
```

<h3 id="token_verify_create-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|[TokenVerify](#schematokenverify)|

<aside class="success">
This operation does not require authentication
</aside>

# Schemas

<h2 id="tocS_Author">Author</h2>
<!-- backwards compatibility -->
<a id="schemaauthor"></a>
<a id="schema_Author"></a>
<a id="tocSauthor"></a>
<a id="tocsauthor"></a>

```json
{
  "id": 0,
  "first_name": "string",
  "last_name": "string",
  "email": "user@example.com",
  "password": "string",
  "password_confirmation": "string",
  "phone": "string",
  "registration_date": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|integer|true|read-only|none|
|first_name|string|false|none|none|
|last_name|string|false|none|none|
|email|string(email)|true|none|none|
|password|string|true|write-only|none|
|password_confirmation|string|true|write-only|none|
|phone|string|true|none|none|
|registration_date|string|true|read-only|none|

<h2 id="tocS_Blog">Blog</h2>
<!-- backwards compatibility -->
<a id="schemablog"></a>
<a id="schema_Blog"></a>
<a id="tocSblog"></a>
<a id="tocsblog"></a>

```json
{
  "author": {
    "id": 0,
    "first_name": "string",
    "last_name": "string",
    "email": "user@example.com",
    "password": "string",
    "password_confirmation": "string",
    "phone": "string",
    "registration_date": "string"
  },
  "title": "string",
  "content": "string",
  "created_at": "2019-08-24T14:15:22Z"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|author|[Author](#schemaauthor)|true|read-only|none|
|title|string|true|none|none|
|content|string|true|none|none|
|created_at|string(date-time)|true|read-only|none|

<h2 id="tocS_Comment">Comment</h2>
<!-- backwards compatibility -->
<a id="schemacomment"></a>
<a id="schema_Comment"></a>
<a id="tocScomment"></a>
<a id="tocscomment"></a>

```json
{
  "author": {
    "id": 0,
    "first_name": "string",
    "last_name": "string",
    "email": "user@example.com",
    "password": "string",
    "password_confirmation": "string",
    "phone": "string",
    "registration_date": "string"
  },
  "blog": 0,
  "content": "string",
  "created_at": "2019-08-24T14:15:22Z"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|author|[Author](#schemaauthor)|true|read-only|none|
|blog|integer|true|none|none|
|content|string|true|none|none|
|created_at|string(date-time)|true|read-only|none|

<h2 id="tocS_PaginatedAuthorList">PaginatedAuthorList</h2>
<!-- backwards compatibility -->
<a id="schemapaginatedauthorlist"></a>
<a id="schema_PaginatedAuthorList"></a>
<a id="tocSpaginatedauthorlist"></a>
<a id="tocspaginatedauthorlist"></a>

```json
{
  "count": 123,
  "next": "http://api.example.org/accounts/?page=4",
  "previous": "http://api.example.org/accounts/?page=2",
  "results": [
    {
      "id": 0,
      "first_name": "string",
      "last_name": "string",
      "email": "user@example.com",
      "password": "string",
      "password_confirmation": "string",
      "phone": "string",
      "registration_date": "string"
    }
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|count|integer|false|none|none|
|next|string(uri)¦null|false|none|none|
|previous|string(uri)¦null|false|none|none|
|results|[[Author](#schemaauthor)]|false|none|none|

<h2 id="tocS_PaginatedBlogList">PaginatedBlogList</h2>
<!-- backwards compatibility -->
<a id="schemapaginatedbloglist"></a>
<a id="schema_PaginatedBlogList"></a>
<a id="tocSpaginatedbloglist"></a>
<a id="tocspaginatedbloglist"></a>

```json
{
  "count": 123,
  "next": "http://api.example.org/accounts/?page=4",
  "previous": "http://api.example.org/accounts/?page=2",
  "results": [
    {
      "author": {
        "id": 0,
        "first_name": "string",
        "last_name": "string",
        "email": "user@example.com",
        "password": "string",
        "password_confirmation": "string",
        "phone": "string",
        "registration_date": "string"
      },
      "title": "string",
      "content": "string",
      "created_at": "2019-08-24T14:15:22Z"
    }
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|count|integer|false|none|none|
|next|string(uri)¦null|false|none|none|
|previous|string(uri)¦null|false|none|none|
|results|[[Blog](#schemablog)]|false|none|none|

<h2 id="tocS_PaginatedCommentList">PaginatedCommentList</h2>
<!-- backwards compatibility -->
<a id="schemapaginatedcommentlist"></a>
<a id="schema_PaginatedCommentList"></a>
<a id="tocSpaginatedcommentlist"></a>
<a id="tocspaginatedcommentlist"></a>

```json
{
  "count": 123,
  "next": "http://api.example.org/accounts/?page=4",
  "previous": "http://api.example.org/accounts/?page=2",
  "results": [
    {
      "author": {
        "id": 0,
        "first_name": "string",
        "last_name": "string",
        "email": "user@example.com",
        "password": "string",
        "password_confirmation": "string",
        "phone": "string",
        "registration_date": "string"
      },
      "blog": 0,
      "content": "string",
      "created_at": "2019-08-24T14:15:22Z"
    }
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|count|integer|false|none|none|
|next|string(uri)¦null|false|none|none|
|previous|string(uri)¦null|false|none|none|
|results|[[Comment](#schemacomment)]|false|none|none|

<h2 id="tocS_PatchedAuthor">PatchedAuthor</h2>
<!-- backwards compatibility -->
<a id="schemapatchedauthor"></a>
<a id="schema_PatchedAuthor"></a>
<a id="tocSpatchedauthor"></a>
<a id="tocspatchedauthor"></a>

```json
{
  "id": 0,
  "first_name": "string",
  "last_name": "string",
  "email": "user@example.com",
  "password": "string",
  "password_confirmation": "string",
  "phone": "string",
  "registration_date": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|integer|false|read-only|none|
|first_name|string|false|none|none|
|last_name|string|false|none|none|
|email|string(email)|false|none|none|
|password|string|false|write-only|none|
|password_confirmation|string|false|write-only|none|
|phone|string|false|none|none|
|registration_date|string|false|read-only|none|

<h2 id="tocS_PatchedBlog">PatchedBlog</h2>
<!-- backwards compatibility -->
<a id="schemapatchedblog"></a>
<a id="schema_PatchedBlog"></a>
<a id="tocSpatchedblog"></a>
<a id="tocspatchedblog"></a>

```json
{
  "author": {
    "id": 0,
    "first_name": "string",
    "last_name": "string",
    "email": "user@example.com",
    "password": "string",
    "password_confirmation": "string",
    "phone": "string",
    "registration_date": "string"
  },
  "title": "string",
  "content": "string",
  "created_at": "2019-08-24T14:15:22Z"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|author|[Author](#schemaauthor)|false|read-only|none|
|title|string|false|none|none|
|content|string|false|none|none|
|created_at|string(date-time)|false|read-only|none|

<h2 id="tocS_PatchedComment">PatchedComment</h2>
<!-- backwards compatibility -->
<a id="schemapatchedcomment"></a>
<a id="schema_PatchedComment"></a>
<a id="tocSpatchedcomment"></a>
<a id="tocspatchedcomment"></a>

```json
{
  "author": {
    "id": 0,
    "first_name": "string",
    "last_name": "string",
    "email": "user@example.com",
    "password": "string",
    "password_confirmation": "string",
    "phone": "string",
    "registration_date": "string"
  },
  "blog": 0,
  "content": "string",
  "created_at": "2019-08-24T14:15:22Z"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|author|[Author](#schemaauthor)|false|read-only|none|
|blog|integer|false|none|none|
|content|string|false|none|none|
|created_at|string(date-time)|false|read-only|none|

<h2 id="tocS_TokenObtainPair">TokenObtainPair</h2>
<!-- backwards compatibility -->
<a id="schematokenobtainpair"></a>
<a id="schema_TokenObtainPair"></a>
<a id="tocStokenobtainpair"></a>
<a id="tocstokenobtainpair"></a>

```json
{
  "email": "string",
  "password": "string",
  "access": "string",
  "refresh": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|email|string|true|write-only|none|
|password|string|true|write-only|none|
|access|string|true|read-only|none|
|refresh|string|true|read-only|none|

<h2 id="tocS_TokenRefresh">TokenRefresh</h2>
<!-- backwards compatibility -->
<a id="schematokenrefresh"></a>
<a id="schema_TokenRefresh"></a>
<a id="tocStokenrefresh"></a>
<a id="tocstokenrefresh"></a>

```json
{
  "access": "string",
  "refresh": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|access|string|true|read-only|none|
|refresh|string|true|write-only|none|

<h2 id="tocS_TokenVerify">TokenVerify</h2>
<!-- backwards compatibility -->
<a id="schematokenverify"></a>
<a id="schema_TokenVerify"></a>
<a id="tocStokenverify"></a>
<a id="tocstokenverify"></a>

```json
{
  "token": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|token|string|true|write-only|none|

