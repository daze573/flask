function test() {
  var obj = document.getElementById("dv1");

  var list = obj.classList;
  console.log(list);

  obj.classList.add("hoge");
  console.log(obj.classList);

  obj.classList.remove("hoge");
  console.log(obj.classList);

  obj.classList.toggle("cs3");
  console.log(obj.classList);
}