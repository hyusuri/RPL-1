package com.nyoba.loginregis.model;

import com.google.gson.annotations.Expose;
import com.google.gson.annotations.SerializedName;

public class DokterModel {
    @SerializedName("success")
    @Expose
    private Integer success;
    @SerializedName("message")
    @Expose
    private String message;
    @SerializedName("iddoc")
    @Expose
    private String iddoc;
    @SerializedName("namadoc")
    @Expose
    private String namadoc;
    @SerializedName("spesialis")
    @Expose
    private String spesialis;
    @SerializedName("idjadwal")
    @Expose
    private String idjadwal;
    @SerializedName("jam")
    @Expose
    private String jam;

    public Integer getSuccess() {
        return success;
    }

    public void setSuccess(Integer success) {
        this.success = success;
    }

    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }

    public String getIddoc() {
        return iddoc;
    }

    public void setIddoc(String iddoc) {
        this.iddoc = iddoc;
    }

    public String getNamadoc() {
        return namadoc;
    }

    public void setNamadoc(String namadoc) {
        this.namadoc = namadoc;
    }

    public String getSpesialis() {
        return spesialis;
    }

    public void setSpesialis(String spesialis) {
        this.spesialis = spesialis;
    }

    public String getIdjadwal() {
        return idjadwal;
    }

    public void setIdjadwal(String idjadwal) {
        this.idjadwal = idjadwal;
    }

    public String getJam() {
        return jam;
    }

    public void setJam(String jam) {
        this.jam = jam;
    }
}
