document.addEventListener("DOMContentLoaded", function() {

  const creatorOptions = {
    showLogicTab: true,
    isAutoSave: true
  };

  function loadSurvey(data) {

    const creator = new SurveyCreator.SurveyCreator(creatorOptions);

    creator.JSON = data

    creator.saveSurveyFunc = (saveNo, callback) => {
      saveSurveyJson(
        "/api/survey",
        creator.JSON,
        saveNo,
        callback
      );
    };

    creator.render("surveyCreator");

  };

  function saveSurveyJson(url, json, saveNo, callback) {

    fetch(
      '/api/survey',
      {
        method: 'POST',
        mode: 'same-origin',
        credentials: 'same-origin',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({'data': json}),
      },
    )
      .then(response => {callback(saveNo, true); console.log(true)})
      .catch(error => {callback(saveNo, false); console.log(false)});

  }

  fetch('/api/survey')
    .then((response) => response.json())
    .then((data) => loadSurvey(data['data']));
});
