unit Unit1;

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, Forms, Controls, Graphics, Dialogs, ComCtrls, DBCtrls,
  ExtCtrls, StdCtrls;

type

  { TMainForm }

  TMainForm = class(TForm)
    Button1: TButton;
    EditTimeWork: TEdit;
    EditTimeRest: TEdit;
    Label1: TLabel;
    Label2: TLabel;
    procedure Button1Click(Sender: TObject);
    procedure Image1Click(Sender: TObject);


  private

  public
    TimeRest:integer;
    TimeWork:integer;

  end;

var
  MainForm: TMainForm;
  n:string ;
  b:Picture;
implementation

{$R *.lfm}

{ TMainForm }

procedure TMainForm.Button1Click(Sender: TObject);
begin
  window.Clear;
  n='Za1.png';
  b:=Picture.Create(n);
  b.Load(n);
  b.Draw(300,50);
end;
end.

