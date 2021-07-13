if count > threshold:
        print(" good part is ", part)
        thres_passed_count += 1
        crop_img = img[startIndexH:startIndexH + new_height - 1, startIndexW:startIndexW + new_width - 1]
        string = str(k) + '-' + str(part)


        #change here !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        cv2.imwrite('D:\pythonProject/' + string + '-crop_img.jpeg', crop_img)