# Large dataset performance test

### Test procedure
Use seed.py to populate a database with data. (No images in this test because I don't want to delete 1000000 images from my drive.)

Go to localhost:5000 with firefox, open the network tab, and in there the timings subtab. Refresh.

Then we continue operating the website as a normal user and noting down the results.

### Test numbers
```
1M Users
500K Listings
1M Comments
```

It took approximately 5 minutes to populate the database. The database file size was 2,21 GB.

The only valuable category in this test was the 'waiting' category and as such all of the following values reference that.
```
GET INDEX:                                                                          1300ms
POST REGISTER:                                                                      123ms
GET LOGIN:                                                                          12ms
POST LOGIN                                                                          123ms
GET INDEX                                                                           1270ms
GET LISTING(ID)                                                                     0ms
GET PROFILE(ID):                                                                    11ms
GET SEARCH BY TITLE and DESC "test":                                                2380ms
GET SORT OLDEST FIRST:                                                              1280ms
GET SORT CATEGORY "BOOKS":                                                          14ms
GET SORT CATEGORY "BOOKS", SORT PRICE LOW TO HIGH:                                  156ms
GET SEARCH BY TITLE and DESC "test", SORT CATEGORY "BOOKS", SORT PRICE LOW TO HIGH: 259ms
```

From this we can conclude that operations which do not have indexes, like filtering using the LIKE operator are much slower than the operations utilizing indexes like using the category.

We can also conclude that the application would perform acceptably at low-size operation, but would significantly struggle even at these tested mid-size numbers. This is because 50 thumbnails would be loaded per page and there would be more than a single concurrent user.