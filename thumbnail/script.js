const percentiles = [25, 50, 75, 100];
const randomize = (bar, arr) => {
  const currHeight = parseInt(bar.style.height.split("%")[0]);
  const filteredArr = arr.filter((height) => height !== currHeight);
  return filteredArr[Math.floor(Math.random() * filteredArr.length)];
};

window.addEventListener("DOMContentLoaded", () => {
  const bars = document.querySelectorAll(".volume-bar");
  setInterval(
    () =>
      bars.forEach(
        (bar) => (bar.style.height = `${randomize(bar, percentiles)}%`)
      ),
    500
  );
});
