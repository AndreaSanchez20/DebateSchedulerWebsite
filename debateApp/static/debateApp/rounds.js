//function to redirect based on value selected
function SelectRedirect(){
    tournamentId = document.getElementById("tournamentCB").value
    switch(document.getElementById("role-select").value){
        case "judge":
            window.location="judge-sign-in/"+ tournamentId;
            break;
        case "student":
            window.location = "dashboard/" + tournamentId;
            break;

    }

}

function showRounds(){
    tournamentId = document.getElementById("tournament").value
    window.location="/dashboard/" + tournamentId;
}

function goToBallot(){
    tournamentId=document.URL.split("/")[4]
    judgeId=document.URL.split("/")[5]
    window.location = "/judge-ballot/"+ tournamentId+ "/"+ judgeId;
}

function goToBallot2(){
    tournamentId=document.URL.split("/")[4]
    judgeId=document.URL.split("/")[5]
    window.location = "/judge-ballot-2/"+ tournamentId+ "/"+ judgeId;
}

function goToDashboardUpdated(){
    tournamentId=document.URL.split("/")[4]
    judgeId=document.URL.split("/")[5]
    result=document.getElementById("result").value
    window.location = "/dashboard/"+ tournamentId+ "/" + judgeId + "/"+ result;
}

function goToJudgeRound(judgeId){
    tournamentId=document.URL.split("/")[4]
    window.location = "/judge-round/"+ tournamentId+ "/"+ judgeId;
}

function goToStudentRound(){
    tournamentId=document.URL.split("/")[4]
    window.location = "/student-round/"+ tournamentId;
}

function getConfirmation(){
    document.getElementById("submit-ballot").onclick=function(){
        window.confirm("You have successfully submitted the ballot");
    }
}
function addNote(){
    tournamentId=document.URL.split("/")[4]
    judgeId=document.URL.split("/")[5]
    note=document.getElementById("area-notes").value
    window.location = "/judge-ballot/"+ tournamentId+ "/"+ judgeId+ "/"+note ;
}