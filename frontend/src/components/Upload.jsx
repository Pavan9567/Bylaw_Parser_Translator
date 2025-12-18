import { useState } from "react";
import { extractPDF } from "../api";

export default function Upload({ onExtracted }) {
    const [file, setFile] = useState(null);
    const [loading, setLoading] = useState(false);

    const handleUpload = async () => {
        if (!file) return alert("Please select a PDF file");

        setLoading(true);

        try {
            const data = await extractPDF(file);
            onExtracted(data);
        } catch (err) {
            alert("Failed to extract PDF");
            console.error(err);
        }
        setLoading(false);
    };

    return (
        <div className="card">
            <div className="step-title">
                <span className="step-badge">STEP 1</span>
                <h2>Upload Bylaw PDF</h2>
            </div>

            <input type="file" accept="application/pdf" onChange={(e) => setFile(e.target.files[0])} />
            <button onClick={handleUpload} disabled={loading}>{loading ? "Extracting..." : "Extract Sections"}</button>
        </div>
    );
}