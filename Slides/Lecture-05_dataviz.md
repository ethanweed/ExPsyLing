---
title: Data Visualization
---



<style>

.reveal h1 { font-size: 2.5em; }


#left {
	margin: 10px 0 15px 0;
	text-align: left;
	float: left;
	z-index:-10;
	width:48%;
	font-size: 0.85em;
	line-height: 1.5; 

}

#right {
	margin: 10px 0 15px 0;
	float: right;
	text-align: left;
	z-index:-10;
	width:48%;
	font-size: 0.85em;
	line-height: 1.5;	
}

#left_border {
	padding: 10px;
	margin: 10px 0 15px 0;
	text-align: left;
	float: left;
	z-index:-10;
	width:48%;
	font-size: 0.85em;
	line-height: 1.5; 
	border: 1px solid #000000;
          border-radius: 10px;
}

#right_border {
	padding: 10px;
	margin: 10px 0 15px 0;
	float: right;
	text-align: left;
	z-index:-10;
	width:48%;
	font-size: 0.85em;
	line-height: 1.5;
	border: 1px solid #000000;
          border-radius: 10px;	
}

#left_border_small {
	padding: 5px;
	margin: 10px 0 15px 0;
	text-align: left;
	float: left;
	z-index:-10;
	width:48%;
	font-size: 0.85em;
	line-height: 1.5; 
	border: 1px solid #000000;
          border-radius: 10px;
}

#right_border_small {
	padding: 5px;
	margin: 10px 0 15px 0;
	float: right;
	text-align: left;
	z-index:-10;
	width:48%;
	font-size: 0.85em;
	line-height: 1.5;
	border: 1px solid #000000;
          border-radius: 10px;	
}

#center_border {
	display: inline-block;
	padding: 1em;
	justify-content: center;
	z-index:-10;
	width:48%;
	font-size: 0.85em;
	line-height: 1.5;
	border: 1px solid #000000;
          border-radius: 10px;	
}

#refs {
	display: inline-block;
	justify-content: left;
	text-align: left;
	z-index:-10;
	width:90%;
	font-size: small;
	line-height: 1.5;	
}

/* mouse over link */
a:hover {
  color: red;
}




</style>

---

# Painting with numbers

---

<img src="https://ethanweed.github.io/pythonbook/_images/snow_ghost_map2.png" width = "600"/>

John Snow’s 1854 map of cholera deaths

---

## Data visualization is a modern invention

<div id = "left">

William Playfair  
(1759-1823)

- Engineer
- Economist
- British secret agent?
- Founder of statistical data visualization
</div>

<div id = "right">

![](https://images.squarespace-cdn.com/content/v1/5b210bafcc8fed1aaffd57aa/1532421067432-6NJ05X3O956WDTJRW2SN/william+playfair.jpg)
</div>


---

## Graphics _reveal_ data

Anscombe’s Quartet

<div id = "left">

<img src="https://github.com/ethanweed/ExPsyLing/blob/master/Slides/Images/Anscombe1.png?raw=true" width=""/>

</div>


<div id = "right">

<img src="https://github.com/ethanweed/ExPsyLing/blob/master/Slides/Images/Anscombe2.png?raw=true" width=""/>

</div>





---


## Garbage in, garbage out

<img src="https://github.com/ethanweed/ExPsyLing/blob/master/Slides/Images/SillyPlot.png?raw=true" width="500"/>

---

## Garbage in, garbage out

<img src="https://github.com/ethanweed/ExPsyLing/blob/master/Slides/Images/SpuriousCorrelation1.png?raw=true" width="600"/>

r = 0.80 ("Strong")

---

#### Graphics tell a _story_

A picture speaks 1888 numbers

<img src="https://github.com/ethanweed/ExPsyLing/blob/master/Slides/Images/TimesWeather.png?raw=true" width=""/>

---

## Graphics tell a _story_

Charles Joseph Minard (1869)

<img src="https://github.com/ethanweed/ExPsyLing/blob/master/Slides/Images/MinardNapaleonsArmy.png?raw=true" width=""/>

<font size="1"> Translation by Dawn Finley, redrawing by Elaine Morse </font>


---

<div id = "left">

<img src="https://github.com/ethanweed/ExPsyLing/blob/master/Slides/Images/MinardNapaleonsArmy.png?raw=true" width=""/>

</div>



<div id = "right">

"It may well be the best statistical graphic ever drawn" - Tufte (2001)

</div>


---


<div id = "left">

<img src="https://github.com/ethanweed/ExPsyLing/blob/master/Slides/Images/MinardNapaleonsArmy.png?raw=true" width=""/>

</div>


<div id = "right">

- Size of the army
- Location of the army
- Direction of the army's movement
- Temperatures during the retreat

</div>


---

<div id = "left">

"It may well be the best statistical graphic ever drawn" - Tufte (2001)

<img src="https://github.com/ethanweed/ExPsyLing/blob/master/Slides/Images/MinardNapaleonsArmy.png?raw=true" width=""/>

</div>


<div id = "right">



"It may well be the worst graphic ever to find its way into print" - Tufte (2001)

<img src="https://github.com/ethanweed/ExPsyLing/blob/master/Slides/Images/TheWorstGraphicEver.png?raw=true" width="300"/>






</div>



---


<img src="https://github.com/ethanweed/ExPsyLing/blob/master/Slides/Images/TheWorstGraphicEver.png?raw=true" width="400"/>


---

## A good graphic provides the most information in the least amount of time


<img src="https://github.com/ethanweed/ExPsyLing/blob/master/Slides/Images/LookingAtPlots.png?raw=true" width=""/>


---

## A good graphic should be honest

$$
\mbox{lie factor} = \frac{\mbox{size of effect shown in graph}}{\mbox{size of effect in data}}
$$


---

Hmm... comparing apples with oranges

<img src="https://github.com/ethanweed/ExPsyLing/blob/master/Slides/Images/LyingChart.png?raw=true" width="300"/>


---

Hmm... no y-axis labels

<img src="https://img.buzzfeed.com/buzzfeed-static/static/2014-10/2/14/enhanced/webdr04/enhanced-buzz-5348-1412276314-10.jpg?downsize=700%3A%2A&output-quality=auto&output-format=auto" width=""/>

---

Hmm... very selective y-axis labels


<img src="https://img.buzzfeed.com/buzzfeed-static/static/2014-10/2/17/enhanced/webdr02/enhanced-buzz-19972-1412285325-16.jpg?downsize=800:*&output-format=auto&output-quality=auto" width=""/>



---

Hmm... again, no y-axis labels

<img src="https://img.buzzfeed.com/buzzfeed-static/static/2014-10/2/17/enhanced/webdr08/enhanced-buzz-21270-1412283681-17.jpg?downsize=800:*&output-format=auto&output-quality=auto" width=""/>


---

Hmm...


<img src="https://preview.redd.it/cxdxeclhueo71.jpg?width=960&crop=smart&auto=webp&s=8135a8bce32516e7b9b0e4ed6c7240a91e6d0bdb" width="550"/>



---

#### Tufte's five principles of data graphics

- Above all else show the data
- Maximize the data to ink ratio
- Erase non-data ink
- Erase redundant data-ink
- Revise and edit


---

#### Maximize data density

$$
\mbox{data density} = \frac{\mbox{number of datapoints}}{\mbox{area of data graphic}}
$$ 

---

Data density = 0.02 numbers per square centimeter

<img src="https://github.com/ethanweed/ExPsyLing/blob/master/Slides/Images/LowDataDensity.png?raw=true" width="400"/>


---


Data density = 28 numbers per square centimeter

<img src="https://github.com/ethanweed/ExPsyLing/blob/master/Slides/Images/TimesWeather.png?raw=true" width="400"/>

---

## Revision

Playfair (1785)

<img src="https://github.com/ethanweed/ExPsyLing/blob/master/Slides/Images/Playfair1.png?raw=true" width="500"/>

---

## Revision

Playfair (1786)

<img src="https://github.com/ethanweed/ExPsyLing/blob/master/Slides/Images/Playfair2.png?raw=true" width="500"/>

---

### An example I'm proud of

<img src="https://github.com/ethanweed/ExPsyLing/blob/master/Slides/Images/RSC-figure.png?raw=true" width=""/>



---


### Another example I'm proud of

<img src="https://github.com/ethanweed/ExPsyLing/blob/master/Slides/Images/ASD_voice_networks.png?raw=true" width=""/>


---


### One last example I'm proud of


<img src="https://github.com/ethanweed/ExPsyLing/blob/master/Slides/Images/Networks2.png?raw=true" width=""/>

---



# References

<div id = "refs">

Tufte, Edward R. The Visual Display of Quantitative Information, Second Edition. Graphics Press: Chesire, Connecticut.


</div>






