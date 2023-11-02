

using System.Linq.Expressions;
using System.Security.Cryptography.X509Certificates;

public class Student {
    private Person _person;
    private Education _education;
    private int _group;
    private Exam[] _exams;

    public Person Per {
        get {return _person; }
        set { _person = value; }
    }

    public Education Ed{
        get { return _education; }
        set { _education = value; }
    }

    public int GroupNumber{
        get { return _group; }
        set { _group = value; }
    }

    public Exam[] Exams {
        get { return _exams; }
        set { _exams = value; }
    }

    public Student(Person person, Education education, int group){
        Per = person;
        Ed = education;
        GroupNumber = group;
    }

    public Student(){
        Per = new Person();
        Ed = Education.Specialist;
        GroupNumber = 1;
        Exams = new[] { new Exam(), new Exam() };
    }

    public double MeanScore{
        get { 
            double sum = Exams.Sum(x => x.Score);            
            return sum / Exams.Length; }
    }

    public bool this [Education ed] {
        get { return Ed == ed; }
    }

    public void AddExams (params Exam[] exams) {
        Exams = Exams.Concat(exams).ToArray();
    }

    public override string ToString()
    {
        string className = base.ToString();
        string person = Per.ToString();
        string education = Ed.ToString();
        string exams = "";

        foreach (var e in Exams) {
            exams += "\t" + e.ToString() + "\n";
        }

        return String.Format("""
        class <{0}>
            Per:    {1}
            Ed:     {2}
            Group:  {3}
            Exams:  
            {4}
        """, className, person, education, GroupNumber, exams);
    }

    public virtual string ToShortString(){
        return String.Format("""
        class <{0}>
            Per:        {1}
            Ed:         {2}
            Group:      {3}
            MeanScore:  {4}
        """, base.ToString(), Per.ToString(), Ed.ToString(), GroupNumber, MeanScore);
    }
}

