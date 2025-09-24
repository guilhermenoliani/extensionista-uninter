import { useEffect, useState } from "react";

function App() {
  const [data, setData] = useState(null);

  useEffect(() => {
    const fetchData = () => {
      fetch("http://localhost:5000/data")
        .then((res) => res.json())
        .then((json) => setData(json))
        .catch((err) =>
          setData({ error: "Não foi possível carregar os dados." })
        );
    };

    fetchData();
    const interval = setInterval(fetchData, 5000);

    return () => clearInterval(interval);
  }, []);

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gradient-to-br from-blue-50 to-indigo-50 p-6">
      <h1 className="text-3xl font-extrabold mb-8 text-gray-800 drop-shadow-md">
        📊 Monitoramento do Sensor DHT11
      </h1>

      {data ? (
        data.error ? (
          <p className="text-red-600 font-semibold text-lg bg-red-100 px-4 py-2 rounded-lg shadow-sm">
            {data.error}
          </p>
        ) : (
          <div className="bg-white shadow-2xl rounded-2xl p-8 w-96 max-w-full text-center border border-gray-200">
            <p className="text-xl font-semibold text-gray-700 mb-4">
              🌡️ Temperatura:{" "}
              <span className="text-red-500">{data.temperature} °C</span>
            </p>
            <p className="text-xl font-semibold text-gray-700 mb-4">
              💧 Umidade:{" "}
              <span className="text-blue-500">{data.humidity} %</span>
            </p>
            <p className="text-xl font-semibold text-gray-700">
              💦 Qualidade da água:{" "}
              <span
                className={`font-bold ${data.water_quality >= 50
                  ? "text-green-600"
                  : "text-red-600"
                  }`}
              >
                {data.water_quality} %
              </span>
            </p>
          </div>
        )
      ) : (
        <p className="text-gray-500 text-lg animate-pulse">
          Carregando dados...
        </p>
      )}
    </div>
  );
}

export default App;
