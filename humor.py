def montar_filas(biblioteca, f_relaxar, f_focar, f_animar, f_treinar):
    f_relaxar.limpar()
    f_focar.limpar()
    f_animar.limpar()
    f_treinar.limpar()

    atual = biblioteca.inicio
    while atual:
        m = atual.musica
        if m.bpm.musica:
            f_relaxar.enqueue(m)
        elif 81 <= m.bpm <= 120:
            f_focar.enqueue(m)
        elif 121 <= m.bpm <= 160:
            f_animar.enqueue(m)
        else:
            f_treinar.enqueue(m)
        atual = atual.proximo