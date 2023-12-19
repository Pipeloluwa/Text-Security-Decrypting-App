package com.example.RAIN;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import androidx.camera.core.CameraSelector;
import androidx.camera.core.ImageCapture;
import androidx.camera.core.ImageCaptureException;
import androidx.camera.core.ImageProxy;
import androidx.camera.core.Preview;
import androidx.camera.lifecycle.ProcessCameraProvider;
import androidx.camera.view.PreviewView;
import androidx.core.app.ActivityCompat;
import androidx.core.content.ContextCompat;
import androidx.lifecycle.LifecycleOwner;

import android.annotation.SuppressLint;
import android.content.pm.PackageManager;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.os.Bundle;
import android.util.SparseArray;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import com.google.android.gms.vision.Frame;
import com.google.android.gms.vision.text.TextBlock;
import com.google.android.gms.vision.text.TextRecognizer;
import com.google.common.util.concurrent.ListenableFuture;

import java.nio.ByteBuffer;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.Executor;


import java.util.Timer;
import java.util.TimerTask;


public class MainActivity extends AppCompatActivity {
    ImageView img;
    Button trap;
    EditText keyE;
    PreviewView previewView;
    TextView textView;
    ImageView screen1;


    private ListenableFuture<ProcessCameraProvider> cameraProviderFuture; //here we have to add the camera provider here
    private ImageCapture imageCapture;
    private int REQUEST_CODE_PERMISSIONS = 1001;
    private final String[] REQUIRED_PERMISSIONS = new String[]{"android.permission.CAMERA"};
    public int a=0;
    ImageView iv;
    Bitmap bitmapImage;
    public String ts;
    int sp= 100; //I can use float as well, in fact float is the default variable type that is meant for it
    int key;
    String pileup="";
    String gather;
    char e;
    String keyE2;
    int suspend=1;
    int nb=0;
    int ck=0;
    int check=0;

    ProcessCameraProvider cameraProvider;


    private boolean allPermissionsGranted(){
        for(String permission : REQUIRED_PERMISSIONS){
            if(ContextCompat.checkSelfPermission(this, permission) != PackageManager.PERMISSION_GRANTED){
                return false;
            }
        }
        return true;
    }
    @Override
    public void onRequestPermissionsResult(int requestCode, @NonNull String[] permissions, @NonNull int[] grantResults) {
        super.onRequestPermissionsResult(requestCode, permissions, grantResults);

        //ts= this.getString(R.string.tx);//one can also use getText which heps to retain any rich text styling applied to the string


        if (requestCode == REQUEST_CODE_PERMISSIONS) {
            if (allPermissionsGranted()) {

                cameraProviderFuture= ProcessCameraProvider.getInstance(this);
                cameraProviderFuture.addListener(() ->{

                    try {
                        ProcessCameraProvider cameraProvider = cameraProviderFuture.get();
                        startCameraX(cameraProvider);
                    }catch (ExecutionException e){
                        e.printStackTrace();
                    }catch (InterruptedException e){
                        e.printStackTrace();
                    }
                },  getExecutor());
            } else {
                Toast.makeText(this, "Permissions not granted by the user.", Toast.LENGTH_SHORT).show();
                this.finish();
            }
        }
    }



    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        previewView= findViewById(R.id.previewView);
        img= findViewById(R.id.img);
        keyE= findViewById(R.id.key);
        textView= findViewById(R.id.textview);
        trap= findViewById(R.id.trap);
        screen1= findViewById(R.id.screen1);

        trap.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if(nb==0){
                    check=1;
                    suspend=0;
                    Toast.makeText(MainActivity.this, "Current Text is trapped", Toast.LENGTH_SHORT).show();
                    nb=1;
                    trap.setText("Untrap Text");
                }else{
                    check=0;
                    suspend=1;
                    Toast.makeText(MainActivity.this, " Text untrapped", Toast.LENGTH_SHORT).show();
                    nb=0;
                }
            }
        });

        if(allPermissionsGranted()){
             //start camera if permission has been granted by user

            cameraProviderFuture= ProcessCameraProvider.getInstance(this);
            cameraProviderFuture.addListener(() ->{

                try {
                    ProcessCameraProvider cameraProvider = cameraProviderFuture.get();
                    startCameraX(cameraProvider);
                }catch (ExecutionException e){
                    e.printStackTrace();
                }catch (InterruptedException e){
                    e.printStackTrace();
                }
            },  getExecutor());
        } else{
            ActivityCompat.requestPermissions(this, REQUIRED_PERMISSIONS, REQUEST_CODE_PERMISSIONS);
        }

    }




    private Executor getExecutor() {
        return ContextCompat.getMainExecutor(this);
    }


    private void startCameraX(ProcessCameraProvider cameraProvider) {
        //Camera Selector use case
        cameraProvider.unbindAll();
        CameraSelector cameraSelector=new CameraSelector.Builder()
                .requireLensFacing(CameraSelector.LENS_FACING_BACK)
                .build();

        //Preview use case
        Preview preview= new Preview.Builder().build();
        preview.setSurfaceProvider(previewView.getSurfaceProvider());

        //Image capture use case
        imageCapture= new ImageCapture.Builder()
                .setCaptureMode(ImageCapture.CAPTURE_MODE_MINIMIZE_LATENCY)
                .build();
        cameraProvider.bindToLifecycle((LifecycleOwner) this, cameraSelector, preview, imageCapture);
        startcustomizedocr(2);
    }


    //I added Timer
    Timer timer;
    class runagain extends TimerTask{
        public void run(){

            //timer.cancel();//Terminates the Timer Thread
            startcustomizedocr(2);
        }

    }

    public void startcustomizedocr(int rt){

        capturePhoto();
        timer= new Timer();
        timer.schedule(new runagain(), rt*1000);
    }
    //I added Timer closed





    private void capturePhoto() {
            imageCapture.takePicture( getExecutor(), new ImageCapture.OnImageCapturedCallback() {
                @SuppressLint("UnsafeOptInUsageError")
                @Override
                public void onCaptureSuccess(@NonNull ImageProxy image) {
                    super.onCaptureSuccess(image);

                    ByteBuffer buffer= image.getPlanes()[0].getBuffer();
                    byte[] bytes= new byte[buffer.capacity()];
                    buffer.get(bytes);
                    bitmapImage= BitmapFactory.decodeByteArray(bytes,0,bytes.length, null);

                    //iv.setRotation((float) image.getImageInfo().getRotationDegrees());
                    //iv.setImageBitmap(bitmapImage);

                    if(ck==0){
                        screen1.setVisibility(View.GONE);
                        //trap.setVisibility(View.VISIBLE);
                        ck=1;
                    }
                    result();

                    //Toast.makeText(MainActivity.this, "Image is captured successfully", Toast.LENGTH_SHORT).show();
                    //Toast.makeText(MainActivity.this, "The format of The Image is "+ image.getFormat() +
                            //" String of the image: "+image.toString(), Toast.LENGTH_LONG).show();
                    //image.getImage();
                    image.close();
                }

                @Override
                public void onError(@NonNull ImageCaptureException exception) {
                    super.onError(exception);
                    //Toast.makeText(MainActivity.this, "in_buffer memory image could not be captured", Toast.LENGTH_SHORT).show();
                }
            });


    }


    public void result () {
        //Bitmap bitmap= BitmapFactory.decodeResource(getApplicationContext().getResources(),R.drawable.aculogo);

        TextRecognizer textRecognizer = new TextRecognizer.Builder(getApplicationContext()).build();

        if (!textRecognizer.isOperational()) {
            Toast.makeText(getApplicationContext(), "Could not get the Text", Toast.LENGTH_SHORT).show();
        } else {


            Frame frame = new Frame.Builder().setBitmap(bitmapImage).build();
            SparseArray<TextBlock> items = textRecognizer.detect(frame);
            StringBuilder sb = new StringBuilder();


            for (int i = 0; i < items.size(); i++) {
                TextBlock myitem = items.valueAt(i);
                //sb.append(myitem.getValue());
                //sb.append("\n");


                //Decryption

                String convert = (myitem.getValue());

                for (int i2 = 0; i2 < convert.length(); i2++) {
                    e = convert.charAt(i2);
                    try{
                        key= Integer.parseInt(keyE.getText().toString());
                        e -= key;
                    }catch (Exception ignored){

                    }

                    gather= Character.toString(e);
                    pileup+=gather;
                }
                sb.append(pileup);
                sb.append("\n");
                pileup= "";

            }

            if(sb.toString().equals("")){
                img.setVisibility(View.VISIBLE);
                if (check!=1){
                    trap.setVisibility(View.GONE);
                }
            }else{
                img.setVisibility(View.INVISIBLE);
                trap.setVisibility(View.VISIBLE);
            }

            if(suspend==1){
                trap.setText("Trap Text");
                textView.setText(sb.toString());
            }
            if(suspend!=1){
                img.setVisibility(View.INVISIBLE);
            }
        }
    }
}