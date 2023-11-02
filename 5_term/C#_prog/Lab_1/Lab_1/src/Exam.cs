public class Exam {
    public string Discipline { get; set; }
    public int Score { get; set; }
    public DateTime Date { get; set; }

    public Exam(string discipline, int score, DateTime date){
        Discipline = discipline;
        Score = score;
        Date = date;
    }

    public Exam(){
        Discipline = "Computer Science";
        var rand = new Random();
        Score = rand.Next(2,5);
        Date = DateTime.Now;
    }

    public override string ToString() {
        return String.Format("class <{0}>:\n\tdiscipline:\t{1}\n\tscore:\t\t{2}\n\tdate:\t\t{3}",base.ToString(), Discipline, Score, Date);
    }
}