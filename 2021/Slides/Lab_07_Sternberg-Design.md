#### Memory scanning task 

**(Sternberg, 1966)**

---

**Research Question: Do people have immediate (parallel) access to all of short-term memory?**

---

**Sternberg (1966) task:**

:::incremental
- Participant is given a list consisting of N digits (N = 1,... , 6)
	- these digits are called the memory set
- The participant is allowed to rehearse this list
- A few seconds later, the participant sees a single digit
	- this number is called the probe
- The participant must indicate whether the probe digit IS or
IS NOT contained in the memory set
:::

---

#### Experiment structure

**Practice block and experimental block**

**Trial structure**

- fixation (1000 ms)
- present memory set (1200 ms)
- ISI (2000 ms)
- present probe (until response)
- feedback (1000 ms)


---

###### Experiment structure

**Stimulus manipulations**  

 - memory set size N = 1,...,6
 - probe present or absent
 - position of probe in list
 - three repetitions of each condition

---

###### Experiment structure

**Experimental trials**

|   N | probe conditions | positions | reps | # trials |
| --: | ---------------: | --------: | ---: | -------: |
|   1 |                2 |         T |    3 |        6 |
|   2 |                2 |         2 |    3 |       12 |
|   3 |                2 |         3 |    3 |       18 |
|   4 |                2 |         4 |    3 |       24 |
|   5 |                2 |         5 |    3 |       30 |
|   6 |                2 |         6 |    3 |       36 |

---

#### Experiment implementation

- Experiment was built using 
	- [OpenSesame](https://osdoc.cogsci.nl) software (Mathôt et al, 2012).
	- [Stimuli](https://github.com/tomfaulkenberry/courses/blob/master/fall2018/psyc5316/README.org) from Tom Faulkenberry
- Experiment files were uploaded to a [JATOS](https://www.jatos.org) server running on a Microsoft Azure virtual machine operated by Aarhus University
- Multi-use links were distributed to participants
- Data were collected in a quiet classroom at Aarhus University

#### Data cleaning pipeline

- Individual responses were downloaded from the server
- Data was converted from the orginal JSON format to csv format with a custom [Python script](https://github.com/ethanweed/ExPsyLing/blob/master/datasets/Sternberg/scripts/convert_jatos2csv.py)
- Data were [cleaned](https://github.com/ethanweed/ExPsyLing/blob/master/datasets/Sternberg/scripts/CleanSternbergData.ipynb) with the following steps:
	- practice trial were removed
	- only correct answers were retained


---

#### References

<font size="2">

	 Lange K, Kühn S, Filevich E (2015) Correction: “Just Another Tool for Online Studies” (JATOS): An Easy Solution for Setup and Management of Web Servers Supporting Online Studies. PLOS ONE 10(7): e0134073.[https://doi.org/10.1371/journal.pone.0134073](https://doi.org/10.1371/journal.pone.0134073)
	
Mathôt, S., Schreij, D., & Theeuwes, J. (2012). OpenSesame: An open-source, graphical experiment builder for the social sciences. _Behavior Research Methods_, _44_(2), 314-324. [doi:10.3758/s13428-011-0168-7](http://dx.doi.org/10.3758/s13428-011-0168-7)
	
Sternberg, S. (1966). High-speed scanning in human memory. _Science_, _153_(3736), 652-654.

- Notes on experiment design from [Tom Faulkenberry](https://www.youtube.com/watch?v=HG8GmhlHOu4)

- The stimuli are taken from Faulkenberry as well: https://github.com/tomfaulkenberry/courses/blob/master/fall2018/psyc5316/README.org

- The same stimuli can be found in the PsychoPy Sternberg demo: https://www.psychopy.org

- The experiment files we used can be found here: https://github.com/ethanweed/OpenSesame/tree/master/Sternberg/experiment_files

- Our original raw data can be found here: https://github.com/ethanweed/ExPsyLing/tree/master/datasets/Sternberg/2021
