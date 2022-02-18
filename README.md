# Surfs Up Analysis
Surf and Ice Cream Shop Analysis for our friend W. Any for the location on Oahu

## Purpose
####
W. Any likes our analysis but wants more info about temperature trends before opening the surf shop. He wants to know temperature data for the months of June and December in Oahu, in order to determine if the surf and ice cream shop business is sustainable year round. We will be creating summary of the statistics for June and a separate summary for December. We will also be delivering a written report for the statistical analyses that is included in this README file.

## Analysis
#### To understand the differences between June and December, I have provided graphs of both months data below. The first being June and the second being December.
> Before we begin our analysis, we should gather the data and charts at our disposal. We have put together histograms and descriptive statistics for both June and December. We should use the charts to observe any obvious behaviors, and reference the descriptive stats to support/reject our hypothesis.

> We also need to understand that I am comparing the 2 months to determine which is better in regards to temperature. If it is an ice cream and surf shop, I would associate better with warmer. Therefore we are going to assume that we are comparing June vs. December to determine which would have better weather according to the criteria I detailed above.

> **Resources for the analysis are attached at the bottom 

#### 5 takeaways from analyzing the resources created from the data
1. The number of temperatures recorded is relatively equal for both months with December having 12 % less recordings to analyze than June. I would be concerned if it were greater than 20% difference.
2. The mean for June is 74 degrees and the mean for December is 71. Those are within 5% of eachother and without feeling what those temperatures there actually feel like, I cannot say that the difference is statistically significant.
3. The top 75% of June is still more than 50% of December. I can see this by referencing the bottom quartile's numbers. June's bottom quartile is 73 degrees making the temperature at or greater than 73 degrees 75% of the time. The mean is 75 degrees.  December has a lower quartile of 69 degrees, and a mean of 71 degrees. June therefore has a hotter lower quartile than December, so 75% of the time June will be at or above 73 degrees, where as December will only be at or above 73 degrees maybe 30/40% of the month.
4. The standard deviation supports our belief in June being the superior month. June has a lower standard deviation than December, meaning there is less likely to be a large variance in June, where as its slightly more likely to have variance in December. 3.26 in June vs. 3.75 in December.
5. Therefore from the data, and from personal experience, we can conclude that June would have better weather more frequently than December would.

#### High Level Summary
* My conclusion is that June is the "better" month given the data we have access to.
* The weather is warmer in June more frequently and more consitenly than it is in December as noted in the analysis points above. The frequency of temperature recordings is greatest around 75 degrees in June, and around 71 in December. We can also see from the descriptive stats that there is a greater chance of having a cold day in December, which would basically foreit all sales for that day. June does not have a good chance of that happening with the lowest low recorded as 64 with December's lowest low being 56.

#### What would help with this analysis?
* 2 Queries I would run would to help with the analysis would be:
    * 1. A query to analyze the precipitation data by date and by station.
    * 2. A query to analyze the distribution of the data by station, because location even on a small island could play a large role in this.
* I would want a the reason for comparing June against December. Our buddy never designates a reason for the analysis, and therefore we are left to assume many things.
* I would want to see data for January and February to compare agaist June, if the reason for the analysis was "trying to compare the peak of summer to the pit of winter". Those to me would seem to be the 2 coldest months that I would want data on to determine if we could be open at all those 2 months. 
* I would also want to see the precipitation data for the dates and also the time of day. We know that temperature follows the basic patter of peaking in the afternoon and bottoming out after midnight in most places around the world. Precipitation in my environment is seemingly random, but I do know that in certain climates around the world it also extremely consistent. Regardless of its assumed distribution, it could be a very helpful addition to this analysis.

##### Resources used in Analysis
<img width="527" alt="Screen Shot 2022-02-18 at 1 47 39 PM" src="https://user-images.githubusercontent.com/95602006/154751889-90b1bbde-e5d4-448f-9539-7271bed1512c.png"> <img width="167" alt="Screen Shot 2022-02-18 at 12 51 52 PM" src="https://user-images.githubusercontent.com/95602006/154751300-c84050f6-8359-4643-ac2f-a2a499cc33c6.png">

<img width="503" alt="Screen Shot 2022-02-18 at 1 50 16 PM" src="https://user-images.githubusercontent.com/95602006/154751948-3fca9e9c-ca7a-4a24-8883-4804fa21ac78.png"> <img width="163" alt="Screen Shot 2022-02-18 at 12 52 01 PM" src="https://user-images.githubusercontent.com/95602006/154751320-b648f302-37a6-4d33-b64d-c9cd2b65d12a.png">


