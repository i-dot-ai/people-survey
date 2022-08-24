Survey.StylesManager.applyTheme("defaultV2");
var json = {};
window.survey = new Survey.Model(json);
survey.onComplete.add(function (sender) {
  document.querySelector('#surveyResult').textContent = "Result JSON:\n" + JSON.stringify(sender.data, null, 3);
});
var storageName = "survey_patient_history";
function saveSurveyData(survey) {
  var data = survey.data;
  data.pageNo = survey.currentPageNo;
  window.localStorage.setItem(storageName, JSON.stringify(data));
}
survey.onPartialSend.add(function (sender) {
  saveSurveyData(sender);
});
survey.onComplete.add(function (sender, options) {
  saveSurveyData(sender);
});
survey.sendResultOnPageNext = true;
var prevData = window.localStorage.getItem(storageName) || null;
if (prevData) {
  var data = JSON.parse(prevData);
  survey.data = data;
  if (data.pageNo) {
    survey.currentPageNo = data.pageNo;
  }
}
$("#surveyElement").Survey({model: survey});
