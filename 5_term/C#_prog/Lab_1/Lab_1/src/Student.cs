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
        _person = person;
        _education = education;
        _group = group;
    }

    public Student(){
        _person = new Person();
        _education = Education.Specialist;
        _group = 1;
        _exams = new[] { new Exam(), new Exam() };
    }

    public double MeanScore{
        get { 
            double sum = _exams.Sum(x => x.Score);            
            return sum / _exams.Length; }
    }

    public bool this [Education ed] {
        get { return _education == ed; }
    }

    public void AddExams (params Exam[] exams) {
        Exams = _exams.Concat(exams).ToArray();
    }

    public override string ToString()
    {
        string exams = "";

        foreach (var e in _exams) {
            exams += "\t" + e.ToString() + "\n";
        }

        return String.Format("""
        class <{0}>
            Per:    {1}
            Ed:     {2}
            Group:  {3}
            Exams:  
            {4}
        """, base.ToString(), _person, _education, _group, exams);
    }

    public virtual string ToShortString(){
        return String.Format("""
        class <{0}>
            Per:        {1}
            Ed:         {2}
            Group:      {3}
            MeanScore:  {4}
        """, base.ToString(), _person, _education, _group, MeanScore);
    }
}

