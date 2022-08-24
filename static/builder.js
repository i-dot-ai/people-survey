const creatorOptions = {
  showLogicTab: true,
  isAutoSave: true
};

function loadSurvey(data) {

  const creator = new SurveyCreator.SurveyCreator(creatorOptions);

  creator.JSON = data

  creator.saveSurveyFunc = (saveNo, callback) => {
    saveSurveyJson(
      "http://localhost:8008/api/survey",
      creator.JSON,
      saveNo,
      callback
    );
  };

  creator.render("surveyCreator");

};

function saveSurveyJson(url, json, saveNo, callback) {
  const request = new XMLHttpRequest();
  request.open('POST', url);
  request.setRequestHeader('Content-Type', 'application/json;charset=UTF-8');
  request.addEventListener('load', () => {
    callback(saveNo, true);
  });
  request.addEventListener('error', () => {
    callback(saveNo, false);
  });
  request.send(JSON.stringify({'data': json}));
}

document.addEventListener("DOMContentLoaded", function() {

  fetch('http://localhost:8008/api/survey')
    .then((response) => response.json())
    .then((data) => loadSurvey(data['data']));
});
