SELECT 
  v.modelo,
  CAST(ROUND(AVG(date_diff('day', f.data_locacao, f.data_entrega)), 2) AS VARCHAR) AS tempo_medio_dias
FROM locadora_catalog.fato_locacoes f
JOIN locadora_catalog.dim_veiculos v ON f.veiculo_id = v.id_veiculo
GROUP BY v.modelo
ORDER BY tempo_medio_dias DESC