<h1 style = "font-family:Utopia;font-size:24px;font-style:regular;text-align:center;">

Demographic Inertia Simulation Report

</h1>


<p style = "font-family:Utopia;font-size:12px;font-style:regular;">

This report was generated at {{date_time}}. 

</p>


<h2 style = "font-family:Utopia;font-size:16px;font-style:regular;">

Model Annotation

</h2>

<p style = "font-family:Utopia;font-size:12px;font-style:regular;">

{{annotation_text}}

</p>

<h2 style = "font-family:Utopia;font-size:16px;font-style:regular;">Model Settings</h2>

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{font-family:Arial, sans-serif;font-size:12px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:black;}
.tg th{font-family:Arial, sans-serif;font-size:12px;font-weight:normal;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:black;}
.tg .tg-fymr{font-weight:bold;border-color:inherit;text-align:left;vertical-align:top}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top}
</style>

<p> Simulation settings by faculty level/gender group.</p>

<table class="tg">
  <tr>
    <th class="tg-fymr"><br>Group</th>
    <th class="tg-fymr">Initial Number<br></th>
    <th class="tg-fymr">Attrition Rate</th>
    <th class="tg-fymr">Hiring Rate</th>
    <th class="tg-fymr">Promotion Rate</th>
  </tr>
  <tr>
    <td class="tg-fymr">Asst. Women</td>
    <td class="tg-0pky">{{number_of_females_1}}<br></td>
    <td class="tg-0pky">{{attrition_rate_women_1}}</td>
    <td class="tg-0pky">{{hiring_rate_women_1}}</td>
    <td class="tg-0pky">{{female_promotion_probability_1}}</td>
  </tr>
  <tr>
    <td class="tg-fymr">Asst. Men<br></td>
    <td class="tg-0pky">{{number_of_males_1}}<br></td>
    <td class="tg-0pky">{{attrition_rate_men_1}}</td>
    <td class="tg-0pky">{{hiring_rate_men_1}}</td>
    <td class="tg-0pky">{{male_promotion_probability_1}}</td>
  </tr>
  <tr>
    <td class="tg-fymr">Assoc. Women</td>
    <td class="tg-0pky">{{number_of_females_2}}</td>
    <td class="tg-0pky">{{attrition_rate_women_2}}</td>
    <td class="tg-0pky">{{hiring_rate_women_2}}</td>
    <td class="tg-0pky">{{female_promotion_probability_2}}</td>
  </tr>
  <tr>
    <td class="tg-fymr">Assoc. Men</td>
    <td class="tg-0pky">{{number_of_males_2}}</td>
    <td class="tg-0pky">{{attrition_rate_men_2}}</td>
    <td class="tg-0pky">{{hiring_rate_men_2}}</td>
    <td class="tg-0pky">{{male_promotion_probability_2}}</td>
  </tr>
  <tr>
    <td class="tg-fymr">Full Women</td>
    <td class="tg-0pky">{{number_of_females_3}}</td>
    <td class="tg-0pky">{{attrition_rate_women_3}}</td>
    <td class="tg-0pky">{{hiring_rate_women_3}}</td>
    <td class="tg-0pky">0.0000</td>
  </tr>
  <tr>
    <td class="tg-fymr">Full Men</td>
    <td class="tg-0pky">{{number_of_males_3}}<br></td>
    <td class="tg-0pky">{{attrition_rate_men_3}}</td>
    <td class="tg-0pky">{{hiring_rate_men_3}}</td>
    <td class="tg-0pky">0.0000</td>
  </tr>
</table>

<p>Simulation settings for overall department</p> 

<table class="tg">
  <tr>
    <th class="tg-fymr"><br>Simulation Duration</th>
    <th class="tg-fymr">Dept. Size Lower Bound<br></th>
    <th class="tg-fymr">Dept. Size Upper Bound</th>
    <th class="tg-fymr">Target Female Prof. Percentage</th>
  </tr>
  <tr>
    <td class="tg-0pky">{{duration}}</td>
    <td class="tg-0pky">{{lowerbound}}<br></td>
    <td class="tg-0pky">{{upperbound}}</td>
    <td class="tg-0pky">{{t_fpct}}</td>
  </tr>
</table>


<h2 style = "font-family:Utopia;font-size:16px;font-style:regular;">Comparison of Model 3 Growth Models: Change in Proportion of Women</h2>


<img src="./images/change_in_percentage_faculty_women.png" alt="drawing" style="width:650px;"/>


<h2 style = "font-family:Utopia;font-size:16px;font-style:regular;">Comparison of Model 3 Growth Models: Probability of Achieving 25% Women</h2>


<img src="./images/probability_of_reaching_gender_target.png" alt="drawing" style="width:650px;"/>



<h2 style = "font-family:Utopia;font-size:16px;font-style:regular;">Comparison of Model 3 Growth Models: Change in Number Women, Model 3</h2>


<img src="./images/change_in_number_women.png" alt="drawing" style="width:650px;"/>



<h2 style = "font-family:Utopia;font-size:16px;font-style:regular;">Comparison of Model 3 Growth Models: Department Size</h2>



<img src="./images/dept_size_plot.png" alt="drawing" style="width:650px;"/>




