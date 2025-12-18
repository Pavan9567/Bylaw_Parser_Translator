import JSONPretty from "react-json-pretty";
import "react-json-pretty/themes/monikai.css";
import { downloadJSON } from "../utils/downloadJson";

export default function Step1View({ data, onTranslate }) {
    if (!data) {
        return null;
    }

    return (
        <div className="card">
            <div className="step-title">
                <span className="step-badge">STEP 1 OUTPUT</span>
                <h2>Extracted Sections</h2>
            </div>

            <div style={{ display: "flex", gap: "10px", marginBottom: "10px" }}>
                <button onClick={onTranslate}>Translate Sections</button>
            </div>

            <button onClick={() => downloadJSON(data, "bylaw_extracted_sections.json")}>Download</button>

            <div className="json-box">
                <JSONPretty data={data} />
            </div>
        </div>
    );
}