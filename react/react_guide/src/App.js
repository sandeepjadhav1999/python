import Expenses from "./components/Expenses/Expenses";
import ExpensFrom from "./components/ExpenseForm/ExpenseFrom";
function App() {
  const expenses = [
    {
      title: "water supply",
      amount: "600",
      date: new Date(2022, 1, 22),
    },
    {
      title: "Electricity bill",
      amount: "1260",
      date: new Date(2022, 6, 1),
    },
    {
      title: "grocery",
      amount: "150",
      date: new Date(2022, 4, 10),
    },
    {
      title: "shoes",
      amount: "3000",
      date: new Date(2022, 9, 24),
    },
  ];
  return (
    <div>
      <ExpensFrom/>
      <Expenses items={expenses} />
    </div>
  );
}

export default App;
