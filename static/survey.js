
function loadSurvey(surveyData, resultData) {

  Survey.StylesManager.applyTheme("defaultV2");

  window.survey = new Survey.Model(surveyData);

  survey.onComplete.add(function (sender) {
    document.querySelector('#surveyResult').textContent = "Result JSON:\n" + JSON.stringify(sender.data, null, 3);
  });

  var storageName = "survey_patient_history";

  function saveSurveyData(survey) {
    var data = survey.data;
    data.pageNo = survey.currentPageNo;

    fetch(
      'http://localhost:8008/api/answer',
      {
        method: 'POST',
        mode: 'same-origin',
        credentials: 'same-origin',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({'data': data}),
      },
    );
  };

  survey.onPartialSend.add(function (sender) {
    saveSurveyData(sender);
  });

  survey.onComplete.add(function (sender, options) {
    saveSurveyData(sender);
  });

  survey.sendResultOnPageNext = true;

  survey.data = resultData;
  if (resultData && resultData.pageNo) {
    survey.currentPageNo = resultData.pageNo;
  };

  $("#surveyElement").Survey({model: survey});

};

document.addEventListener("DOMContentLoaded", function() {
  Promise.all([
    fetch('http://localhost:8008/api/survey').then(resp => resp.json()),
    fetch('http://localhost:8008/api/answer').then(resp => resp.json()),
  ]).then((result) => loadSurvey(result[0]['data'], result[1]['data']))
});
