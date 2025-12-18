import axios from "axios";

const API_BASE = "http://localhost:8000";

export const extractPDF = async (file) => {
    const formData = new FormData();
    formData.append("file", file);

    const response = await axios.post(
        `${API_BASE}/extract`,
        formData,
        {headers: { "Content-Type": "multipart/form-data" }}
    );

    return response.data;
};

export const translateSections = async (sections) => {
    const response = await axios.post(
        `${API_BASE}/translate`,
        sections,
        { headers: { "Content-Type": "application/json" } }
    );

    return response.data;
};