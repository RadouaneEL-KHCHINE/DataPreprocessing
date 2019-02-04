with open("tornik-map-20171006.10000.tsv", "r", encoding="utf-8") as tornikF:

    viewMode0 = ""

    with open("result.tsv", "w", encoding="utf-8") as resultTornikF:

        for line in tornikF.readlines():
            try:

                target = line.split("\t")[1].split('/')

                if target[1] == "map":

                    viewMode = target[4]
                    zoomLevel = target[6]

                    if viewMode == viewMode0:
                        numVM = numVM + 1
                        zoomArr.append(zoomLevel)
                    else:
                        if viewMode0 != "":
                            resultTornikF.write("\t".join([viewMode0, str(numVM), ",".join(zoomArr)])+"\n")

                        viewMode0 = viewMode
                        zoomArr = [zoomLevel]
                        numVM = 1

            except:
                pass

        # Pour écrire le dérnier résultat
        resultTornikF.write("\t".join([viewMode0, str(numVM), ",".join(zoomArr)])+"\n")
