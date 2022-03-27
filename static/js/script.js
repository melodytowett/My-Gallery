function myFuntion(){
    var copyText = document.getElementById("myImage");
    /*select the text field*/
    copyText.Select();
    copyText.setSelectionrange(0,99999);
    /*copy text to clipboard */
    navigator.clipboard.writeText(copyText.value);
    /*alert copied text */
    var tooltip = document.getElementById("mytooltip");
    tooltip.innerHTML = "Copied:" + copyText.value;
}
function outFunc(){
    var tooltip = document.getElementById("myTooltip");
    tooltip.innerHTML = "Copy to clipboard";
}