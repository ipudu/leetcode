update Requests
set status = 'Closed'
where AptID in (select AptID from Apartments where BuildingID = 11);