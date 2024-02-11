// See https://aka.ms/new-console-template for more information
//Console.WriteLine("Hello, World!");

using System.Collections;

var dt = DateTime.Now;

var per1 = new Person(name: "x", surname:"y", birthday:dt);
var per2 = new Person(name: "x", surname:"y", birthday:dt);
var per3 = new Person(name: "Monkey", surname:"D. Luffy", birthday:DateTime.Now);


var ex1 = new Exam(discipline: "dfdf", score: 4, dt);
var ex2 = new Exam(discipline: "dfdf", score: 4, dt);
var ex3 = new Exam();

var st1 = new Student();
st1.Per = per1;
st1.Exams = new[] {ex1, ex2};
var st2 = new Student();
st2.Per = per2;
st2.Exams = new[] {ex1, ex2};
var st3 = new Student(per3, Education.Specialist, 3);


// переопределение Equals
var str = "\t Person \t Student \t Exam \n";
var str2 = String.Format("\neq \t {0} \t\t {1} \t\t {2}", per1.Equals(per2), st1.Equals(st2), ex1.Equals(ex2));
var str3 = String.Format("\nnot eq \t {0} \t\t {1} \t\t {2}", per1.Equals(per3), st1.Equals(st3), ex1.Equals(ex3));
var str4 = String.Format("\nhash 1\t {0}\t{1}\t{2}", per1.GetHashCode(), st1.GetHashCode(), ex1.GetHashCode());
var str5 = String.Format("\nhash 2\t {0}\t{1}\t{2}", per2.GetHashCode(), st2.GetHashCode(), ex2.GetHashCode());
var str6 = String.Format("\nhash 3\t {0}\t{1}\t{2}", per3.GetHashCode(), st3.GetHashCode(), ex3.GetHashCode());



Console.WriteLine(str + str2 + str3 + str4 + str5 + str6);