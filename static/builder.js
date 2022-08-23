const creatorOptions = {
    showLogicTab: true,
    isAutoSave: true
};

const creator = new SurveyCreator.SurveyCreator(creatorOptions);

document.addEventListener("DOMContentLoaded", function() {
    creator.render("surveyCreator");
});

creator.saveSurveyFunc = (saveNo, callback) => {
    window.localStorage.setItem("survey-json", creator.text);
    callback(saveNo, true);

};
