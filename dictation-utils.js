/* Ελληνικά ordered dictation comparison. Dependency-free, browser and Node compatible. */
(function (root) {
  "use strict";
  const strip = (s) => String(s || "").normalize("NFD").replace(/[\u0300-\u036f]/g, "").normalize("NFC").toLocaleLowerCase("el-GR")
    .replace(/ς/g, "σ").replace(/[^\p{L}\p{N}]+/gu, "");
  function compare(target, typed) {
    const a = target.map(strip), b = typed.map(strip).filter(Boolean);
    const n = a.length, m = b.length;
    const dp = Array.from({ length: n + 1 }, () => new Uint16Array(m + 1));
    for (let i = n - 1; i >= 0; i--) for (let j = m - 1; j >= 0; j--)
      dp[i][j] = a[i] && a[i] === b[j] ? 1 + dp[i + 1][j + 1] : Math.max(dp[i + 1][j], dp[i][j + 1]);
    let i = 0, j = 0;
    const matched = [];
    while (i < n && j < m) {
      if (a[i] && a[i] === b[j]) { matched.push(i); i++; j++; }
      else if (dp[i + 1][j] >= dp[i][j + 1]) i++;
      else j++;
    }
    return { correct: matched.length, total: n, matched, score: n ? matched.length / n : 0 };
  }
  const api = { compare, strip };
  if (typeof module !== "undefined" && module.exports) module.exports = api;
  root.EllinikaDictation = api;
})(typeof window !== "undefined" ? window : globalThis);
