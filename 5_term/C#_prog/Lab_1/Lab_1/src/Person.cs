public class Person{
    private readonly string _name;
    private readonly string _surname;
    private DateTime _birthday;

    public Person(string name, string surname, DateTime birthday){
        _name = name;
        _surname = surname;
        _birthday = birthday;
    }

    public Person(){
        _name = "John";
        _surname = "Doe";
        _birthday = DateTime.Now;
    }

    public string Name {
        get { return _name; }
    }

    public string Surname {
        get { return _surname; }
    }

    public DateTime Birthday {
        get { return _birthday; }
    }

    public int Year {
        get { return _birthday.Year; }
        set { _birthday = new DateTime(value, _birthday.Month, _birthday.Day); }
    }

    public override string ToString() {
        return String.Format("class <{0}>:\n\tname:\t\t{1}\n\tsurname:\t{2}\n\tbirthay:\t{3}",base.ToString(), Name, Surname, Birthday);
    }

    public virtual string ToShortString() {
        return String.Format("{0} {1}", Name, Surname);
    }

}


