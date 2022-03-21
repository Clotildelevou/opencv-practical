#include <opencv2/imgcodecs.hpp>
#include <opencv2/imgproc.hpp>
#include <opencv2/highgui.hpp>

#include <iostream>
#include <vector>
#include <string>

using namespace cv;

int main(int argc, char** argv)
{
    std::vector<std::string> args (argv, argv + argc);
    
    Mat img = imread(args[1]);
    Mat img_gray;
    cvtColor(img, img_gray, COLOR_BGR2GRAY);

    // apply binary thresholding
    Mat thresh;
    threshold(img_gray, thresh, 100, 255, THRESH_BINARY);
    imshow("Result", thresh);
    waitKey(0);
    imwrite("results/image_thres1.jpg", thresh);
    destroyAllWindows();
}
