# polling-place-closures
An exploration of polling place closures based on data from the Center for Public Integrity &amp; Stateline.

The goal of this project is to examine the rate of polling place closures in states previously held to the VRA's Section 4(b) preclearance formula requirement after the 2013 Shelby v Holder ruling.

[The following states](https://www.justice.gov/crt/jurisdictions-previously-covered-section-5), as a whole, had been subject to preclearance before the ruling

- Alabama
- Alaska
- Arizona
- Georgia
- Louisiana
- Mississippi
- South Carolina
- Texas
- Virginia

## Running this project

This project was created using Python 3.7.5, and using this version minimizes the likelihood of compatibility issues.

To install dependencies  for this project, run the following:

```bash
pip install -r requirements.txt
```

## Rough Outline

- For all states:
  - Determine if there exists enough data
  - Remove noisy states
  - For all non-noisy states:
    - Get data for 2012
    - Get data for 2018
    - Generate table of closed polling places
    - Compute stats on polling closures

- For state in preclearance_states_with_data:
  - Get data for 2012
  - Get data for 2018
  - Generate table of closed polling places
  - Compute stats on polling closures

def generateTable
- determine unique indetifier for polling place

def ComputeStats

## Preclearence States, as of 07/11/2021

|State         |2012 - General |2014 – General |2016 – General |2018 – General |
|--------------|---------------|---------------|---------------|---------------|
|Alabama       |Awaiting Review|Awaiting Review|Awaiting Review|Awaiting Review|
|Alaska        |Released       |Released       |Released       |Released       |
|Arizona       |Awaiting Review|Awaiting Review|Awaiting Review|Awaiting Review|
|Georgia       |Awaiting Review|Awaiting Review|Released       |Released       |
|Louisiana     |Released       |Released       |Released       |Released       |
|Mississippi   |Released       |Released       |Released       |Released       |
|South Carolina|Released       |Released       |Released       |Released       |
|Texas         |Awaiting Review|Awaiting Review|Awaiting Review|Awaiting Review|
|Virginia      |Released       |Released       |Released       |Released       |

Based on the table above – a subset of the data in STATUS.md – the following states have data available for analysis:

- Alaska (2012-2018)
- Georgia (2016-2018)
- Louisiana (2012-2018)
- Mississippi (2012-2018)
- South Carolina (2012-2018)
- Virginia (2012-2018)

## States with Released Data, 07/11/2021

|State         |2012 - General |2014 – General |2016 – General |2018 – General |
|--------------|---------------|---------------|---------------|---------------|
|Alaska        |Released       |Released       |Released       |Released       |
|Arkansas      |Released       |Released       |Missing        |Released       |
|Connecticut   |Released       |Released       |Released       |Released       |
|Delaware      |Released       |Released       |Released       |Released       |
|Georgia       |Awaiting Review|Awaiting Review|Released       |Released       |
|Illinois      |Released       |Released       |Released       |Released       |
|Iowa          |Released       |Released       |Released       |Released       |
|Kentucky      |Released       |Released       |Released       |Released       |
|Louisiana     |Released       |Released       |Released       |Released       |
|Maine         |Released       |Released       |Released       |Released       |
|Maryland      |Released       |Released       |Released       |Released       |
|Massachusetts |Released       |Released       |Released       |Released       |
|Michigan      |Released       |Released       |Missing        |Missing        |
|Minnesota     |Data Entry     |Released       |Released       |Released       |
|Mississippi   |Released       |Released       |Released       |Released       |
|Montana       |Released       |Released       |Released       |Released       |
|Nebraska      |Released       |Released       |Released       |Released       |
|New Hampshire |Released       |Released       |Missing        |Released       |
|New Jersey    |Released       |Released       |Released       |Released       |
|New Mexico    |Awaiting Review|Released       |Released       |Released       |
|North Carolina|Released       |Released       |Released       |Released       |
|North Dakota  |Released       |Released       |Released       |Released       |
|Ohio          |Released       |Released       |Released       |Released       |
|Oklahoma      |Released       |Released       |Released       |Released       |
|Pennsylvania  |Released       |Released       |Released       |Released       |
|Rhode Island  |Released       |Released       |Released       |Released       |
|South Carolina|Released       |Released       |Released       |Released       |
|South Dakota  |Released       |Released       |Released       |Released       |
|Utah          |Released       |Released       |Released       |Released       |
|Vermont       |Released       |Released       |Released       |Released       |
|Virginia      |Released       |Released       |Released       |Released       |
|West Virginia |Released       |Released       |Released       |Released       |
|Wisconsin     |Released       |Released       |Released       |Released       |

Based on the table above – a subset of the data in STATUS.md – the following states have data available for analysis:

- Alaska
- Arkansas
- Connecticut
- Delaware
- Georgia
- Illinois
- Iowa
- Kentucky
- Louisiana
- Maine
- Maryland
- Massachusetts
- Michigan
- Minnesota
- Mississippi
- Montana
- Nebraska
- New Hampshire
- New Jersey
- New Mexico
- North Carolina
- North Dakota
- Ohio
- Oklahoma
- Pennsylvania
- Rhode Island
- South Carolina
- South Dakota
- Utah
- Vermont
- Virginia
- West Virginia
- Wisconsin