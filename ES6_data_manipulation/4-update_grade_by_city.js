export default function updateGradeByCity(students, city, newGrade) {
  return students.filter((student) => student.location === city)
    .map((student) => {
      const studentGrade = newGrade.find((grade) => grade.studentId === student.id);
      if (studentGrade) {
        return { ...student, grade: studentGrade.grade };
      }
      return student;
    });
}
