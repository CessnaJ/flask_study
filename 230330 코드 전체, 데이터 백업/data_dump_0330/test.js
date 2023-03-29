const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
  event.preventDefault();
  try {
    const formData = new FormData();
    const body = {
      spot: {
        spotName: registerData.registerMap.spotName,
        spotAddress: state?.address,
        spotBuildingName: registerData.registerMap.spotBuildingName,
        spotCategory: registerData.registerMap.spotCategory,
        spotTelNumber: registerData.registerMap.spotTelNumber,
        spotLat: state?.lat,
        spotLng: state?.lng,
      },
      sfInfos: registerData.registerMap.checkedList,
    };
    Array.from(selectedFiles).forEach((temp) =>
      formData.append("spotImages", temp)
    );
    const json = JSON.stringify(body);
    const blob = new Blob([json], { type: "application/json" });
    formData.append("spotDto", blob);
    const response = await axios.post(
      "http://192.168.31.134:8080/api/spot/save",
      formData,
      {
        headers: {
          "Content-Type": "multipart/form-data",
          Authorization: `Bearer ${localStorage.getItem("accessToken")}`,
        },
      }
    );
    // console.log(response);
  } catch (err) {
    console.error(err);
  }
};
