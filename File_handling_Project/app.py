import streamlit as st
from pathlib import Path
import os
from datetime import datetime

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="FileVault",
    page_icon="🗂️",
    layout="centered",
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');

/* Reset & base */
html, body, [class*="css"] {
    font-family: 'Space Grotesk', sans-serif;
}

/* Dark slate background */
.stApp {
    background-color: #0f1117;
    color: #e2e8f0;
}

/* Hide Streamlit chrome */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 2rem; padding-bottom: 2rem; max-width: 720px; }

/* ── Hero header ── */
.hero {
    text-align: center;
    padding: 2.5rem 0 2rem;
    border-bottom: 1px solid #1e2535;
    margin-bottom: 2rem;
}
.hero-icon {
    font-size: 2.8rem;
    display: block;
    margin-bottom: 0.5rem;
}
.hero h1 {
    font-size: 2.6rem;
    font-weight: 700;
    letter-spacing: -1px;
    color: #f0f4ff;
    margin: 0;
    line-height: 1;
}
.hero h1 span {
    color: #6c8bff;
}
.hero p {
    color: #64748b;
    font-size: 0.95rem;
    margin: 0.6rem 0 0;
    letter-spacing: 0.02em;
}

/* ── Operation cards ── */
.op-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 0.75rem;
    margin-bottom: 2rem;
}
.op-card {
    background: #161b27;
    border: 1px solid #1e2535;
    border-radius: 12px;
    padding: 1rem 0.5rem;
    text-align: center;
    cursor: pointer;
    transition: all 0.18s ease;
}
.op-card:hover {
    border-color: #6c8bff;
    background: #1a2140;
    transform: translateY(-2px);
}
.op-card.active {
    border-color: #6c8bff;
    background: #1a2140;
    box-shadow: 0 0 0 1px #6c8bff, 0 4px 20px rgba(108,139,255,0.15);
}
.op-icon { font-size: 1.5rem; display: block; margin-bottom: 0.4rem; }
.op-label { font-size: 0.78rem; font-weight: 600; color: #94a3b8; letter-spacing: 0.06em; text-transform: uppercase; }

/* ── Panel ── */
.panel {
    background: #161b27;
    border: 1px solid #1e2535;
    border-radius: 16px;
    padding: 1.75rem;
    margin-bottom: 1rem;
}
.panel-title {
    font-size: 1.1rem;
    font-weight: 600;
    color: #c7d2fe;
    margin-bottom: 1.25rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

/* ── Status messages ── */
.msg-success {
    background: #0d2818;
    border: 1px solid #22c55e;
    border-left: 4px solid #22c55e;
    border-radius: 8px;
    padding: 0.85rem 1rem;
    color: #86efac;
    font-size: 0.9rem;
    margin-top: 1rem;
}
.msg-error {
    background: #2a0f0f;
    border: 1px solid #ef4444;
    border-left: 4px solid #ef4444;
    border-radius: 8px;
    padding: 0.85rem 1rem;
    color: #fca5a5;
    font-size: 0.9rem;
    margin-top: 1rem;
}
.msg-info {
    background: #0c1a2e;
    border: 1px solid #3b82f6;
    border-left: 4px solid #3b82f6;
    border-radius: 8px;
    padding: 0.85rem 1rem;
    color: #93c5fd;
    font-size: 0.9rem;
    margin-top: 1rem;
}

/* ── File content display ── */
.file-content {
    background: #0a0e17;
    border: 1px solid #1e2535;
    border-radius: 8px;
    padding: 1rem;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.82rem;
    color: #a5f3fc;
    line-height: 1.7;
    margin-top: 1rem;
    white-space: pre-wrap;
    max-height: 280px;
    overflow-y: auto;
}
.file-meta {
    font-size: 0.78rem;
    color: #475569;
    font-family: 'JetBrains Mono', monospace;
    margin-top: 0.5rem;
}

/* ── Inputs ── */
div[data-testid="stTextInput"] > div > div > input {
    background: #0a0e17 !important;
    border: 1px solid #1e2535 !important;
    border-radius: 8px !important;
    color: #e2e8f0 !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 0.88rem !important;
}
div[data-testid="stTextInput"] > div > div > input:focus {
    border-color: #6c8bff !important;
    box-shadow: 0 0 0 2px rgba(108,139,255,0.2) !important;
}
div[data-testid="stTextArea"] textarea {
    background: #0a0e17 !important;
    border: 1px solid #1e2535 !important;
    border-radius: 8px !important;
    color: #e2e8f0 !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 0.85rem !important;
}
div[data-testid="stTextArea"] textarea:focus {
    border-color: #6c8bff !important;
    box-shadow: 0 0 0 2px rgba(108,139,255,0.2) !important;
}

/* ── Buttons ── */
.stButton > button {
    background: #6c8bff !important;
    color: #fff !important;
    border: none !important;
    border-radius: 8px !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-weight: 600 !important;
    font-size: 0.88rem !important;
    padding: 0.55rem 1.4rem !important;
    transition: all 0.15s ease !important;
    letter-spacing: 0.02em !important;
}
.stButton > button:hover {
    background: #5a78f0 !important;
    transform: translateY(-1px) !important;
    box-shadow: 0 4px 14px rgba(108,139,255,0.35) !important;
}

/* ── Radio buttons ── */
div[data-testid="stRadio"] label {
    color: #94a3b8 !important;
    font-size: 0.88rem !important;
}
div[data-testid="stRadio"] div[role="radio"] {
    accent-color: #6c8bff;
}

/* ── Select box ── */
div[data-testid="stSelectbox"] > div > div {
    background: #0a0e17 !important;
    border: 1px solid #1e2535 !important;
    border-radius: 8px !important;
    color: #e2e8f0 !important;
}

/* ── Divider ── */
hr { border-color: #1e2535; }

/* ── File list pills ── */
.file-pill {
    display: inline-block;
    background: #1e2535;
    border-radius: 6px;
    padding: 0.3rem 0.7rem;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.8rem;
    color: #a5f3fc;
    margin: 0.2rem;
}

/* ── Footer ── */
.footer {
    text-align: center;
    color: #334155;
    font-size: 0.78rem;
    margin-top: 3rem;
    padding-top: 1.5rem;
    border-top: 1px solid #1e2535;
}
</style>
""", unsafe_allow_html=True)

# ── Session state defaults ────────────────────────────────────────────────────
if "operation" not in st.session_state:
    st.session_state.operation = "Create"
if "feedback" not in st.session_state:
    st.session_state.feedback = None   # ("success"|"error"|"info", message)

# ── Helpers ──────────────────────────────────────────────────────────────────
WORKSPACE = Path("workspace")
WORKSPACE.mkdir(exist_ok=True)

def safe_path(name: str) -> Path:
    """Resolve to workspace-relative path, reject path traversal."""
    p = (WORKSPACE / name).resolve()
    if not str(p).startswith(str(WORKSPACE.resolve())):
        raise ValueError("Invalid path")
    return p

def list_files():
    return sorted([f.name for f in WORKSPACE.iterdir() if f.is_file()])

def fmt_bytes(n):
    return f"{n} B" if n < 1024 else f"{n/1024:.1f} KB"

# ── Hero ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
  <span class="hero-icon">🗂️</span>
  <h1>File<span>Vault</span></h1>
  <p>Create · Read · Update · Delete — right from your browser</p>
</div>
""", unsafe_allow_html=True)

# ── Operation selector ────────────────────────────────────────────────────────
ops = [("✦ Create", "Create"), ("◎ Read", "Read"), ("⟳ Update", "Update"), ("✕ Delete", "Delete")]
cols = st.columns(4)
for col, (label, op) in zip(cols, ops):
    with col:
        active_class = "active" if st.session_state.operation == op else ""
        st.markdown(f"""
        <div class="op-card {active_class}" onclick="">
          <span class="op-icon">{label.split()[0]}</span>
          <span class="op-label">{op}</span>
        </div>
        """, unsafe_allow_html=True)

selected_op = st.radio(
    "Operation", [o[1] for o in ops],
    index=[o[1] for o in ops].index(st.session_state.operation),
    horizontal=True, label_visibility="collapsed"
)
if selected_op != st.session_state.operation:
    st.session_state.operation = selected_op
    st.session_state.feedback = None
    st.rerun()

st.markdown("<hr>", unsafe_allow_html=True)

# ── Workspace file browser (sidebar pill list) ────────────────────────────────
files = list_files()
if files:
    pills = "".join(f'<span class="file-pill">📄 {f}</span>' for f in files)
    st.markdown(f"""
    <div style="margin-bottom:1.5rem;">
      <div style="font-size:0.75rem;font-weight:600;color:#475569;letter-spacing:0.08em;text-transform:uppercase;margin-bottom:0.5rem;">Workspace files</div>
      {pills}
    </div>
    """, unsafe_allow_html=True)

# ── CREATE ────────────────────────────────────────────────────────────────────
if selected_op == "Create":
    st.markdown('<div class="panel"><div class="panel-title">✦ Create a new file</div>', unsafe_allow_html=True)
    file_name = st.text_input("File name", placeholder="e.g. notes.txt", key="c_name")
    file_content = st.text_area("File content", placeholder="Type your content here...", height=160, key="c_content")
    if st.button("Create File", key="c_btn"):
        if not file_name.strip():
            st.session_state.feedback = ("error", "Please enter a file name.")
        else:
            try:
                p = safe_path(file_name.strip())
                if p.exists():
                    st.session_state.feedback = ("error", f"'{file_name}' already exists in the workspace.")
                else:
                    p.write_text(file_content)
                    st.session_state.feedback = ("success", f"'{file_name}' created successfully — {fmt_bytes(len(file_content.encode()))} written.")
            except Exception as e:
                st.session_state.feedback = ("error", str(e))
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# ── READ ──────────────────────────────────────────────────────────────────────
elif selected_op == "Read":
    st.markdown('<div class="panel"><div class="panel-title">◎ Read a file</div>', unsafe_allow_html=True)
    if files:
        file_name = st.selectbox("Choose a file", files, key="r_name")
    else:
        file_name = st.text_input("File name", placeholder="e.g. notes.txt", key="r_name_txt")
    content_holder = st.empty()
    if st.button("Read File", key="r_btn"):
        fn = file_name if isinstance(file_name, str) else file_name
        if not fn:
            st.session_state.feedback = ("error", "Please select or enter a file name.")
        else:
            try:
                p = safe_path(fn)
                if not p.exists():
                    st.session_state.feedback = ("error", f"'{fn}' does not exist.")
                else:
                    text = p.read_text()
                    stat = p.stat()
                    mtime = datetime.fromtimestamp(stat.st_mtime).strftime("%d %b %Y, %H:%M")
                    st.session_state.feedback = ("read_result", (fn, text, fmt_bytes(stat.st_size), mtime))
            except Exception as e:
                st.session_state.feedback = ("error", str(e))
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

    if st.session_state.feedback and st.session_state.feedback[0] == "read_result":
        fn, text, size, mtime = st.session_state.feedback[1]
        st.markdown(f"""
        <div class="msg-info">📄 Showing <strong>{fn}</strong></div>
        <div class="file-content">{text if text else "(empty file)"}</div>
        <div class="file-meta">Size: {size} &nbsp;·&nbsp; Last modified: {mtime}</div>
        """, unsafe_allow_html=True)

# ── UPDATE ────────────────────────────────────────────────────────────────────
elif selected_op == "Update":
    st.markdown('<div class="panel"><div class="panel-title">⟳ Update a file</div>', unsafe_allow_html=True)
    if files:
        file_name = st.selectbox("Choose a file", files, key="u_name")
    else:
        file_name = st.text_input("File name", placeholder="e.g. notes.txt", key="u_name_txt")

    action = st.radio(
        "Update action",
        ["Rename", "Append content", "Overwrite content"],
        horizontal=True, key="u_action"
    )

    if action == "Rename":
        new_name = st.text_input("New file name", placeholder="e.g. renamed.txt", key="u_newname")
        if st.button("Rename File", key="u_btn"):
            fn = file_name
            if not fn or not new_name.strip():
                st.session_state.feedback = ("error", "Please provide both current and new file names.")
            else:
                try:
                    p = safe_path(fn)
                    np = safe_path(new_name.strip())
                    if not p.exists():
                        st.session_state.feedback = ("error", f"'{fn}' does not exist.")
                    elif np.exists():
                        st.session_state.feedback = ("error", f"'{new_name}' already exists.")
                    else:
                        p.rename(np)
                        st.session_state.feedback = ("success", f"Renamed '{fn}' → '{new_name}'.")
                except Exception as e:
                    st.session_state.feedback = ("error", str(e))
            st.rerun()

    elif action == "Append content":
        append_data = st.text_area("Content to append", height=120, key="u_append")
        if st.button("Append to File", key="u_btn"):
            fn = file_name
            try:
                p = safe_path(fn)
                if not p.exists():
                    st.session_state.feedback = ("error", f"'{fn}' does not exist.")
                else:
                    with open(p, "a") as f:
                        f.write("\n" + append_data)
                    st.session_state.feedback = ("success", f"Content appended to '{fn}'.")
            except Exception as e:
                st.session_state.feedback = ("error", str(e))
            st.rerun()

    else:  # Overwrite
        new_data = st.text_area("New content (replaces everything)", height=120, key="u_overwrite")
        if st.button("Overwrite File", key="u_btn"):
            fn = file_name
            try:
                p = safe_path(fn)
                if not p.exists():
                    st.session_state.feedback = ("error", f"'{fn}' does not exist.")
                else:
                    p.write_text(new_data)
                    st.session_state.feedback = ("success", f"'{fn}' overwritten successfully.")
            except Exception as e:
                st.session_state.feedback = ("error", str(e))
            st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)

# ── DELETE ────────────────────────────────────────────────────────────────────
elif selected_op == "Delete":
    st.markdown('<div class="panel"><div class="panel-title">✕ Delete a file</div>', unsafe_allow_html=True)
    if files:
        file_name = st.selectbox("Choose a file to delete", files, key="d_name")
    else:
        file_name = st.text_input("File name", placeholder="e.g. notes.txt", key="d_name_txt")

    st.markdown("""
    <div style="background:#2a0f0f;border:1px solid #7f1d1d;border-radius:8px;padding:0.75rem 1rem;font-size:0.82rem;color:#fca5a5;margin:1rem 0;">
      ⚠️ This action is <strong>permanent</strong> and cannot be undone.
    </div>
    """, unsafe_allow_html=True)

    confirm = st.checkbox("Yes, I want to permanently delete this file", key="d_confirm")
    if st.button("Delete File", key="d_btn"):
        fn = file_name
        if not confirm:
            st.session_state.feedback = ("error", "Please check the confirmation box first.")
        else:
            try:
                p = safe_path(fn)
                if not p.exists():
                    st.session_state.feedback = ("error", f"'{fn}' does not exist.")
                else:
                    p.unlink()
                    st.session_state.feedback = ("success", f"'{fn}' deleted permanently.")
            except Exception as e:
                st.session_state.feedback = ("error", str(e))
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# ── Feedback banner ───────────────────────────────────────────────────────────
if st.session_state.feedback and st.session_state.feedback[0] in ("success", "error"):
    kind, msg = st.session_state.feedback
    css_class = "msg-success" if kind == "success" else "msg-error"
    icon = "✓" if kind == "success" else "✗"
    st.markdown(f'<div class="{css_class}">{icon} {msg}</div>', unsafe_allow_html=True)

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="footer">
  Built with Python + Streamlit &nbsp;·&nbsp; FileVault
</div>
""", unsafe_allow_html=True)