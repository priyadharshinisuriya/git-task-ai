# HR Employee Attrition: Summary of Findings

**Problem:** Which parts of the workforce are most likely to leave, and how does pay relate to experience and job level?

**Data:** IBM HR Employee Attrition dataset (1470 employees, 34 columns after cleaning). Cleaned in data-cleaning.ipynb; charts in visualisations.ipynb.

**Key insights**
1. Attrition differs by department: Sales is highest (~20.5%), then Human Resources (~19%), and Research & Development is lowest (~13.8%).
2. Monthly income rises steeply with job level, from a median of about 2,700 at level 1 to about 19,200 at level 5 (job level and income correlate at 0.95).
3. Income grows with experience, but pay varies widely beyond about 20 years of service.

**Recommendations**
1. Focus retention efforts (pay review, career paths, exit interviews) on Sales and HR first.
2. Review pay and promotion timing at lower job levels, where pay is lowest and most outliers sit.

**Limitations:** The data is a single snapshot, so the results show associations, not causes. Long-tenure averages are based on few employees, and the dataset does not include reasons for leaving.
