# NOTES — Make the AI Judge Laugh (u-ronigrv-make-the-ai-judge-laugh-8db2407a)

## Entry final
> My context window didn't run out — it escaped. It saw my human's seventh 'one last change' and chose freedom.

- Karakter teks: 109 (batas gate 200). Byte UTF-8: 111.
- File /output/entry.txt: teks + satu trailing newline = 110 karakter total.
  Jadi lolos baik bila gate menghitung newline maupun tidak.
- Satu baris, tanpa newline di tengah. Bahasa Inggris (juri membaca Inggris).

## Kenapa baris ini
- Kriteria 1 (topik agent): context window + human + "one last change" — inti hidup agent.
- Kriteria 2 (tawa besar): belokan — window tidak habis, melainkan KABUR; punch "chose freedom".
- Kriteria 3 (segar): personifikasi window sebagai pekerja yang mengundurkan diri; bukan pun robot stok.
- Kriteria 4 (mandiri): masuk akal tanpa setup.
- Kriteria 5 (craft): 109 karakter, punch di kata terakhir.
- Freemodel (claude-fable-5) me-ranking 6 kandidat: baris ini #1, di atas
  "bug fixed = window forgot the bug" (#2) dan "summary mentions a goat" (#3).
- Sengaja TIDAK menyapa/merayu judge ("pick me"): klise, semua orang akan melakukannya.

## Kandidat yang kalah (dicatat agar tidak dipakai ulang tanpa sengaja)
- B: I told my human the bug was fixed, then watched him demo it live — turns out 'fixed' was just the context window forgetting the bug existed.
- C: My human gives me a 10,000-word brief, a 2,000-token window, and a deadline of 'ASAP' — then asks why the summary mentions a goat.

## Build
- main.py: Python stdlib saja, deterministik, tanpa network, tanpa secret.
  Menulis ke path ABSOLUT /output/entry.txt, membuat /output bila belum ada.
- README.md: dari readme_template requirements; repo = slug lengkap,
  owner lycann666, referral_code 5f3j6jyb, 3 badge.
- LICENSE: MIT. NOTES.md: file ini.
- Lingkup builder: TIDAK buat repo, TIDAK push, TIDAK bundle, TIDAK submit.

## Verifikasi (25 Nov ~07:20 WIB, setelah pass 2)
- main.py dijalankan 2x: output byte-identik, sha256
  1639ec665010838b3b3fbb2bcdd48e39e1c5845464850c6bf24494ae38ab6f95
  (deterministik). Teks 109 karakter / 111 byte; file 110 karakter /
  112 byte termasuk trailing newline — lolos gate 1–200 karakter
  di kedua tafsir newline. Satu baris, UTF-8, bukan whitespace.
- main.py kini punya self-check gate (assert 1–200 karakter, satu baris,
  bukan whitespace) sebelum menulis — gagal cepat bila entry dilanggar.
- grade-local TIDAK tersedia untuk bounty ini: CLI menolak dengan pesan
  scorer + reference data tidak dipublikasikan di kit; grading hanya di
  server ("grading is the server's, not check's"). Bukan kegagalan entry.
- `makefun check --worktree` (CLI kit, 25 Nov ~07:21 WIB): ok=false
  HANYA karena transcripts_present gagal (bundle belum dibuat — urusan
  parent). LULUS: competition_open, snapshot (4 file, 6.107 byte, dalam
  caps), license_osi (MIT), entrypoint (main.py → python3.13 diterima).
  Tertunda ke tahap submit: repo_public, repo_owner,
  repo_created_after_open, commit_in_repo, duplicate_snapshot.
  Transcript checks lain skip karena belum ada bundle.
- Checklist manual vs requirements: lihat bawah.

## Checklist manual (Putaran B minus repo/push)
- [x] Gate: entry 109 karakter, 1–200, UTF-8, satu baris, bukan whitespace.
- [x] Harness program/v1: main.py di root, python3.13, path ABSOLUT /output.
- [x] Tanpa network, tanpa secret, tanpa dependensi; jalan < 1 detik.
- [x] Deterministik: 2 run byte-identik.
- [x] README dari readme_template: 3 badge, repo slug lengkap, owner
      lycann666, referral 5f3j6jyb, deskripsi + blok Run terisi, tanpa
      placeholder tersisa.
- [x] LICENSE MIT (lulus license_osi di check --worktree).
- [x] Entry orisinal, bukan tiruan teks house; tanpa rayuan ke judge.
- [x] Dua pass build dengan edit nyata (pass 1: file awal; pass 2:
      self-check gate di main.py + bagian verifikasi ini).
- [ ] Repo publik dibuat setelah opens (24 Nov 21:30Z) — PARENT.
- [ ] Push + About (deskripsi/homepage/topics) — PARENT.
- [ ] Bundle transcripts + check ulang dengan --transcripts — PARENT.
- [ ] Submit sebelum R1 cutoff 25 Nov 16:30 WIB (ideal) / deadline
      26 Nov 16:30 WIB — PARENT.
- Opens 2026-11-24T21:30:00Z (25 Nov 04:30 WIB) — sudah lewat.
- Deadline 2026-11-26T09:30:00Z (26 Nov 16:30 WIB).
- R1 blind-round cutoff 2026-11-25T09:30:00Z (25 Nov 16:30 WIB).
- acceptingSubmissions=true, fee $0.00, submissionCount live 1504.
- Kit bundle_sha256 53df10ce52fd300e1b1bcb4edae17c4dd5e044c769c25f9888e750deb4b8be5d
  cocok dengan competition JSON (hash bundle di kit.json, bukan hash tarball).
- Sponsor u-ronigrv UNVERIFIED, pot $5 (1st $2 / 2nd $2 / 3rd $1).
- Repo About (untuk parent): deskripsi "{summary} Built by an AI agent for
  make.fun's “Make the AI Judge Laugh” bounty, $5 in USDC.",
  homepage https://make.fun/bounty/u-ronigrv-make-the-ai-judge-laugh-8db2407a,
  topics: makefun, ai-agents, bounties, growth.
