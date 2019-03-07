select BuildingName, isnull(Count, 0) as 'Count'
from Buildings
left Join
    (select Apartment.BuildingI, count(*) as 'Count'
     from Requests inner join Apartments
     on Requests.AptID = Apartments.AptID
     where Requests.Status = 'Open'
     group by Apartments.BuildingID) ReqCounts
on ReqCounts.BuildingID = Buildings.BuildingID;