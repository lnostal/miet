
using System.Diagnostics;

Student PrintStudent(Student student){
    Console.WriteLine(student.ToShortString());
    Console.WriteLine();
    return student;
}

void CheckEducation(Student student){
    Console.WriteLine(student[Education.Specialist]);
    Console.WriteLine(student[Education.Вachelor]);
    Console.WriteLine(student[Education.SecondEducation]);
    Console.WriteLine();
}


void SetVars(Student student){
    student.Per = new Person(name: "Spike", surname: "Spiegel", birthday: DateTime.Now);
    student.Ed = Education.SecondEducation;
    student.GroupNumber = 6;
    student.Exams = new[] { new Exam(), new Exam(), new Exam() };
    Console.WriteLine(student.ToString());
    Console.WriteLine();
}

void AddExams(Student student){
    student.AddExams(new[] { new Exam(discipline: "Math", score: 3, date: DateTime.Now) });
    Console.WriteLine(student.ToString());
    Console.WriteLine();
}


void CompareTicks(){
    var separators = new[] {" ", ",", "*", "x"};

    Console.WriteLine("Enter nrow and ncolumn using one of separators: [{0}]", String.Join("] [", separators));
    var str = Console.ReadLine();

    var sep = separators.First(x => str.Contains(x));
    var nums = str.Split(sep);

    Benchmark(int.Parse(nums[0]), int.Parse(nums[1]));
}

void Benchmark(int nrow, int ncolumn){

    var arrD =  OneDemention(nrow, ncolumn);
    var arr2D = TwoDementions_Rectangular(nrow, ncolumn);
    var arr2DS = TwoDementions_Step(nrow, ncolumn);

    var watch1D = Stopwatch.StartNew(); 
    foreach (var s in arrD){
            someAction(s);
        }
    watch1D.Stop(); 

    var watch2D = Stopwatch.StartNew(); 
    foreach (var s in arr2D){
        someAction(s);
    }
    watch2D.Stop(); 

    var watch2DS = Stopwatch.StartNew(); 
    foreach (var s in arr2DS){
        foreach (var ss in s) {
            someAction(ss);
        }
    }
    watch2DS.Stop(); 


    Console.WriteLine("Compare setting GroupNumber");
    Console.WriteLine("Arr[]: " + watch1D.ElapsedTicks);
    Console.WriteLine("Arr[,]: " + watch2D.ElapsedTicks);
    Console.WriteLine("Arr[][]: " + watch2DS.ElapsedTicks);

}

Student[] OneDemention(int nrow, int ncolumn){
    int countOfElements = nrow * ncolumn;

    return Enumerable.Range(0, countOfElements)
                    .Select(_ => new Student())
                    .ToArray();
}

Student[,] TwoDementions_Rectangular(int nrow, int ncolumn){
    
    Student[,] arr = new Student[nrow,ncolumn];
    
    for (int i = 0;  i < nrow; i++){
        for (int j = 0;  j < ncolumn; j++){
            arr[i,j] = new Student();
        }
    }

    return arr;
}

Student[][] TwoDementions_Step(int nrow, int ncolumn){

    int column1 = nrow > ncolumn ? nrow % ncolumn : ncolumn % nrow;
    int column2 = nrow > ncolumn ? nrow / ncolumn : ncolumn / nrow;
    int column3 = nrow * ncolumn - column1 - column2;

    Student[][] arr = new Student[3][];
    arr[0] = Enumerable.Range(0, column1)
                    .Select(_ => new Student())
                    .ToArray();
    arr[1] = Enumerable.Range(0, column2)
                    .Select(_ => new Student())
                    .ToArray();
    arr[2] = Enumerable.Range(0, column3)
                    .Select(_ => new Student())
                    .ToArray();

    return arr;
}


void someAction(Student st){
    st.Ed = Education.Вachelor;
}

/*
Создать один объект типа Student, преобразовать данные в текстовый
вид с помощью метода ToShortString() и вывести данные.
*/
//var student = new Student();
//PrintStudent(student);

/*
Вывести значения индексатора для значений индекса Education.Specialist,
Education.Bachelor и Education.SecondEducation.
*/
//CheckEducation(student);

/*
Присвоить значения всем определенным в типе Student свойствам,
преобразовать данные в текстовый вид с помощью метода ToString() и
вывести данные.
*/
//SetVars(student);

/*
C помощью метода AddExams( params Exam*+ ) добавить элементы в
список экзаменов и вывести данные объекта Student, используя метод
ToString().
*/
//AddExams(student);

/*
Сравнить время выполнения операций с элементами одномерного,
двумерного прямоугольного и двумерного ступенчатого массивов с
одинаковым числом элементов типа Exam.

Значения nrow и ncolumn вводятся в процессе работы приложения в виде
одной строки с разделителями. 
*/
CompareTicks();

