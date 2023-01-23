# Casbin

- https://pypi.org/project/asynccasbin/
```
import casbin
e = casbin.Enforcer("path/to/model.conf", "path/to/policy.csv")
```
## Enforcement Code
```
## We should get the below from the database form of ID or role or etc.
sub = "alice"  # the user that wants to access a resource.
obj = "data1"  # the resource that is going to be accessed.
act = "read"  # the operation that the user performs on the resource.


if e.enforce(sub, dom, obj, act):
    # permit alice to read data1
    pass
else:
    # deny the request, show an error
    pass
```

## Type of Models
- ACL - Access Control List
- RBAC - Role Based Access Control
- ABAC - Attribute Based Access Control

## Example RBAC
```
[request_definition]
r = sub,, obj, act

[policy_definition]
p = sub, obj, act

[role_definition]
g = _, _

[policy_effect]
e = some(where (p.eft == allow))

[matchers]
m = g(r.sub, p.sub) && r.obj == p.obj && r.act == p.act
```

## Policy
- This will vary depending on your definition in the model. For rbac with domains it will take the below form
- p = sub,  obj, act
```
p, role::admin, data1, read
p, role::relationship_manager, data1, read
p, role::accounting, data1, read
p, role::finance, data1, read

```
