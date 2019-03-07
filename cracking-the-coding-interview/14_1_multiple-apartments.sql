select TenantName
from Tenants
inner join (select TenantID from AptTenants group by TenantID having count(*) > 1) C
on Tenants.TenantID = C.TenantID;