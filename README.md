# Overview

This document outlines the Oracle APEX application that was developed to visualize and analyze casino activities. The dashboard provides a graphical representation of data related to game types, monthly revenue, and player statistics.

![Casino Activities Main](Casino%20Activities%20Main.png)

# Dashboard Section with SQL Queries and JS

### Average Bet by Game Type

![GameType](GameType.png)

To analyze the betting patterns across different games, we use the following SQL query to calculate the average bet amount for each game type. The results are ordered by the average bet in descending order to identify which games have the highest stakes.

```sql
SELECT
  "GAMETYPE",
  AVG("BETAMOUNT") AS "AVERAGE_BET"
FROM
  CASINO_ACTIVITY
GROUP BY
  "GAMETYPE"
ORDER BY
  AVG("BETAMOUNT") DESC;
```

### Monthly Casino Revenue

![House Revenue](House%20Revenue.png)

Understanding the revenue trends is crucial for the casino's financial analysis. The following SQL query provides the net revenue for each month by summing up the win/loss amounts.

```sql
SELECT
  TO_CHAR(TRUNC(TO_DATE("DATETIME", 'MM/DD/YYYY')), 'YYYY-MM') AS "MONTH",
  -SUM("WINLOSSAMOUNT") AS "MONTHLY_REVENUE"
FROM
  CASINO_ACTIVITY
GROUP BY
  TO_CHAR(TRUNC(TO_DATE("DATETIME", 'MM/DD/YYYY')), 'YYYY-MM')
ORDER BY
  "MONTH" ASC;
```

### Top Frequent Player Nets

![Top Frequent Player Nets](Top%20Frequent%20Player%20Nets.png)

Identifying the players who frequent the casino the most and their net winnings is valuable for customer relationship management. This SQL query selects the top 10 players based on the frequency of their visits and their total winnings. The JavaScript snippet  is used to prepend a ranking number to player IDs on the chart. This helps in quickly identifying the top players in the visual representation.

```sql
SELECT
  "PLAYERID",
  COUNT("PLAYERID") AS "Frequency",
  SUM("WINLOSSAMOUNT") AS "Total_Winnings"
FROM
  CASINO_ACTIVITY
GROUP BY
  "PLAYERID"
ORDER BY
  "Frequency" DESC
FETCH FIRST 10 ROWS ONLY;
```
```javascript
// Assign X Values
// Ensure this runs after the chart is fully rendered
apex.jQuery(function($) {
  // Target the chart container by its Static ID
  var chartContainerId = 'R45844629039383693872_jet';

  // Find all text elements within the chart container
  var textElements = $('#' + chartContainerId + ' text');

  // Loop through each text element starting from index 10 and prepend the ranking
  textElements.each(function(index) {
    if (index >= 10) { // Assuming index 10 and onwards are the Player IDs
      var currentText = $(this).text();
      var newText = '#' + (index - 9) + ' ID' + currentText; // index - 9 to start counting from 1
      $(this).text(newText);
    }
  });
});

```


### Misc

The following was used to run a diagnotsit for extracting elements from a container. Helpful with newer projects and manipulating elements manually.
// Diagnostic script to log information about the chart's text elements

```javascript
var chartContainer = document.querySelector('#ENTERCONTAINERIDHERE');
if (chartContainer) {
  console.log('Chart container found:', chartContainer);

  var textElements = chartContainer.querySelectorAll('text');
  console.log('Number of text elements in the chart:', textElements.length);

  textElements.forEach(function(text, index) {
    console.log(`Text element ${index}:`, text.textContent, ' - ID:', text.id);
  });
} else {
  console.log('Chart container not found.');
}
```

### Other Reports

Searches through the example data generated as well as the data itself all available for viewing and running new dynamic reports.

![APEX 3](APEX_3.png)

![APEX 4](APEX_4.png)
