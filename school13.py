import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Seaborn Style
sns.set_style("whitegrid")


class StudentPerformanceAnalysis:

    # Constructor
    def __init__(self, file_path):
        self.df = pd.read_excel("school.xlsx")

    # Display Dataset
    def show_data(self):
        print("\n========== FIRST 5 RECORDS ==========")
        print(self.df.head())

    # Statistics Analysis
    def statistics(self):

        print("\n========== STATISTICAL ANALYSIS ==========")

        avg_marks = np.mean(self.df["Marks"])
        max_marks = np.max(self.df["Marks"])
        min_marks = np.min(self.df["Marks"])

        avg_attendance = np.mean(
            self.df["Attendance_Percent"]
        )

        print(f"Average Marks : {avg_marks:.2f}")
        print(f"Maximum Marks : {max_marks}")
        print(f"Minimum Marks : {min_marks}")
        print(f"Average Attendance : {avg_attendance:.2f}")

    # Top Students
    def top_students(self):

        print("\n========== TOP 5 STUDENTS ==========")

        top = self.df.nlargest(5, "Marks")

        print(top[["Student_Name", "Marks"]])

    # Class-wise Analysis
    def class_analysis(self):

        print("\n========== CLASS-WISE ANALYSIS ==========")

        result = self.df.groupby("Class").agg({
            "Marks": "mean",
            "Attendance_Percent": "mean"
        })

        print(result)

    # Dashboard with 4 Subplots
    def dashboard(self):

        fig, axes = plt.subplots(2, 2, figsize=(14, 10))

        # ==================================
        # Graph 1 : Marks Distribution
        # ==================================

        sns.histplot(
            self.df["Marks"],
            bins=10,
            kde=True,
            color="skyblue",
            ax=axes[0, 0]
        )

        axes[0, 0].set_title("Marks Distribution")
        axes[0, 0].set_xlabel("Marks")
        axes[0, 0].set_ylabel("Frequency")

        # ==================================
        # Graph 2 : Attendance vs Marks
        # ==================================

        sns.scatterplot(
            x="Attendance_Percent",
            y="Marks",
            data=self.df,
            color="red",
            s=80,
            ax=axes[0, 1]
        )

        axes[0, 1].set_title("Attendance vs Marks")
        axes[0, 1].set_xlabel("Attendance %")
        axes[0, 1].set_ylabel("Marks")

        # ==================================
        # Graph 3 : Average Marks by Class
        # ==================================

        class_avg = self.df.groupby("Class")["Marks"].mean()

        axes[1, 0].bar(
            class_avg.index.astype(str),
            class_avg.values,
            color=["orange", "green", "purple"]
        )

        axes[1, 0].set_title("Average Marks by Class")
        axes[1, 0].set_xlabel("Class")
        axes[1, 0].set_ylabel("Average Marks")

        # ==================================
        # Graph 4 : Attendance Boxplot
        # ==================================

        sns.boxplot(
            x="Class",
            y="Attendance_Percent",
            data=self.df,
            palette="Set2",
            ax=axes[1, 1]
        )

        axes[1, 1].set_title("Class-wise Attendance")
        axes[1, 1].set_xlabel("Class")
        axes[1, 1].set_ylabel("Attendance %")

        # Main Title

        plt.suptitle(
            "Student Performance Analysis Dashboard",
            fontsize=18,
            fontweight="bold"
        )

        plt.tight_layout()
        plt.show()


# ==========================================
# MAIN PROGRAM
# ==========================================

if __name__ == "__main__":

    obj = StudentPerformanceAnalysis("school.xlsx")

    obj.show_data()

    obj.statistics()

    obj.top_students()

    obj.class_analysis()

    obj.dashboard()